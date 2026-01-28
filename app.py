from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import json
import os
import uuid
import random
from datetime import datetime

app = Flask(__name__)
CORS(app)

DB_FILE = "db.json"


def load_db():
    if not os.path.exists(DB_FILE):
        return {"stations": [], "bookings": [], "partners": []}
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_db(db):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2)


@app.route("/")
def home():
    return send_from_directory(".", "index.html")


@app.route("/api/stations")
def stations():
    db = load_db()
    return jsonify({"stations": db.get("stations", [])})


@app.route("/api/bookings")
def bookings():
    db = load_db()
    return jsonify({"bookings": db.get("bookings", [])})


@app.route("/api/book", methods=["POST"])
def book():
    payload = request.json or {}
    station_id = payload.get("station_id")
    slot = payload.get("slot")
    vehicle_number = payload.get("vehicle_number")
    from_time = payload.get("from_time")
    to_time = payload.get("to_time")
    payment_mode = payload.get("payment_mode")
    amount = payload.get("amount")

    if not station_id or not slot or not vehicle_number:
        return jsonify({"success": False, "message": "Missing required fields"}), 400

    db = load_db()
    stations = db.get("stations", [])
    station = next((s for s in stations if s["id"] == station_id), None)

    if not station:
        return jsonify({"success": False, "message": "Station not found"}), 404

    booked_slots = station.get("booked_slots", 0)
    if booked_slots >= station.get("slots", 0):
        return jsonify({"success": False, "message": "No slots available"}), 409

    station["booked_slots"] = booked_slots + 1

    otp = str(random.randint(1000, 9999))

    booking = {
        "booking_id": str(uuid.uuid4())[:8].upper(),
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "station_id": station_id,
        "station_name": station["name"],
        "slot": slot,
        "vehicle_number": vehicle_number,
        "from_time": from_time,
        "to_time": to_time,
        "payment_mode": payment_mode,
        "amount": amount,
        "payment_status": "PENDING",
        "otp": otp,
        "otp_verified": False,
        "status": "CONFIRMED"
    }

    db["bookings"].append(booking)
    save_db(db)

    return jsonify({"success": True, "booking": booking})


@app.route("/api/payment_simulate", methods=["POST"])
def payment_simulate():
    payload = request.json or {}
    booking_id = payload.get("booking_id")

    db = load_db()
    booking = next((b for b in db.get("bookings", []) if b["booking_id"] == booking_id), None)
    if not booking:
        return jsonify({"success": False, "message": "Booking not found"}), 404

    # Random SUCCESS / FAILED simulation
    booking["payment_status"] = random.choice(["SUCCESS", "FAILED"])
    save_db(db)

    return jsonify({"success": True, "booking": booking})


@app.route("/api/otp_verify", methods=["POST"])
def otp_verify():
    payload = request.json or {}
    booking_id = payload.get("booking_id")
    otp = payload.get("otp")

    db = load_db()
    booking = next((b for b in db.get("bookings", []) if b["booking_id"] == booking_id), None)
    if not booking:
        return jsonify({"success": False, "message": "Booking not found"}), 404

    if str(booking.get("otp")) == str(otp):
        booking["otp_verified"] = True
        save_db(db)
        return jsonify({"success": True, "booking": booking})

    return jsonify({"success": False, "message": "Invalid OTP"}), 401


@app.route("/api/qr_validate", methods=["POST"])
def qr_validate():
    payload = request.json or {}
    booking_id = payload.get("booking_id")

    db = load_db()
    booking = next((b for b in db.get("bookings", []) if b["booking_id"] == booking_id), None)
    if not booking:
        return jsonify({"success": False, "message": "Booking not found"}), 404

    if booking.get("payment_status") != "SUCCESS":
        return jsonify({"success": False, "message": "Payment not successful"}), 403

    if booking.get("otp_verified") is not True:
        return jsonify({"success": False, "message": "OTP not verified"}), 403

    return jsonify({"success": True, "booking": booking})


@app.route("/api/reset_station/<station_id>", methods=["POST"])
def reset_station(station_id):
    db = load_db()
    station = next((s for s in db.get("stations", []) if s["id"] == station_id), None)
    if not station:
        return jsonify({"success": False, "message": "Station not found"}), 404

    station["booked_slots"] = 0
    save_db(db)
    return jsonify({"success": True, "message": "Station reset done"})


# -------- ADMIN APIs --------
@app.route("/api/admin/add_station", methods=["POST"])
def admin_add_station():
    payload = request.json or {}

    db = load_db()

    new_id = "ST" + str(random.randint(100, 999))

    station = {
        "id": new_id,
        "name": payload.get("name"),
        "type": payload.get("type"),
        "price": payload.get("price"),
        "slots": payload.get("slots"),
        "booked_slots": 0,
        "city": payload.get("city"),
        "area": payload.get("area"),
        "lat": payload.get("lat"),
        "lng": payload.get("lng")
    }

    db["stations"].append(station)

    partner = {
        "partner_id": str(uuid.uuid4())[:6].upper(),
        "partner_name": f"{station['name']} Partner",
        "station_id": station["id"],
        "station_name": station["name"],
        "type": station["type"],
        "slots": station["slots"],
        "price": station["price"],
        "onboarded_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    if "partners" not in db:
        db["partners"] = []

    db["partners"].append(partner)
    save_db(db)

    return jsonify({"success": True, "station": station, "partner": partner})


@app.route("/api/admin/partners")
def admin_partners():
    db = load_db()
    return jsonify({"partners": db.get("partners", [])})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

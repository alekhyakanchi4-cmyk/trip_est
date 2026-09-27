from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Average mileage presets (km per liter)
VEHICLE_MILEAGE = {
    "bike": 40.0,
    "hatchback": 18.0,
    "sedan": 14.0,
    "suv": 10.0,
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/calculate-trip", methods=["POST"])
def calculate_trip():
    data = request.get_json() or {}

    try:
        distance_km = float(data.get("distance_km", 0))
        persons = int(data.get("persons", 1))
        days = int(data.get("days", 1))
        vehicle_type = str(data.get("vehicle_type", "hatchback")).lower()
        fuel_price = float(data.get("fuel_price", 100))
        stay_cost_per_room = float(data.get("stay_cost_per_day", 2000))
        food_cost_per_person = float(data.get("food_cost_per_day", 500))
        misc_cost = float(data.get("misc_cost", 1000))
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid numerical parameters supplied."}), 400

    if distance_km <= 0 or persons <= 0 or days <= 0:
        return jsonify({"error": "Distance, persons, and days must be greater than zero."}), 400

    mileage = VEHICLE_MILEAGE.get(vehicle_type, 15.0)
    total_fuel_liters = (distance_km * 2) / mileage
    fuel_expense = total_fuel_liters * fuel_price

    rooms_needed = (persons + 1) // 2
    stay_expense = rooms_needed * stay_cost_per_room * days

    food_expense = persons * food_cost_per_person * days

    grand_total = fuel_expense + stay_expense + food_expense + misc_cost
    per_person_cost = grand_total / persons

    return jsonify({
        "currency": "INR",
        "currency_symbol": "₹",
        "inputs": {
            "round_trip_distance_km": distance_km * 2,
            "persons": persons,
            "days": days,
            "vehicle_type": vehicle_type,
            "estimated_mileage_kpl": mileage,
        },
        "breakdown": {
            "Fuel": round(fuel_expense, 2),
            "Stay/Hotel": round(stay_expense, 2),
            "Food & Dining": round(food_expense, 2),
            "Tolls & Misc": round(misc_cost, 2),
        },
        "grand_total": round(grand_total, 2),
        "per_person_cost": round(per_person_cost, 2),
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

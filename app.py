
from flask import Flask, render_template, request
import os

app = Flask(__name__)

# 오늘의 재료 (예시)
ingredients = ["계란", "양파", "토마토", "닭고기", "치즈"]

# 요리 추천 로직
def recommend_dishes(selected_ingredients):
    rules = {
        frozenset(["계란", "양파"]): "계란 오믈렛",
        frozenset(["토마토", "치즈"]): "카프레제 샐러드",
        frozenset(["닭고기", "양파"]): "닭볶음탕",
        frozenset(["계란", "토마토"]): "토마토 계란 볶음",
    }
    for ing_set, dish in rules.items():
        if ing_set.issubset(selected_ingredients):
            return dish
    return "추천 가능한 요리가 없습니다."

@app.route("/", methods=["GET", "POST"])
def index():
    selected_ingredients = []
    dish = None
    if request.method == "POST":
        selected_ingredients = request.form.getlist("ingredients")
        dish = recommend_dishes(set(selected_ingredients))
    return render_template("index.html", ingredients=ingredients, dish=dish)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def get_legal_response(user_input):
    """
    Expanded rule-based legal responses for offline use.
    Covers Constitution, Articles, Fundamental Rights, Duties, DPSPs, and landmark cases.
    """
    user_input_lower = user_input.lower()

    # Constitution basics
    if "constitution" in user_input_lower:
        return ("The Constitution of India is the supreme law of the country. "
                "It came into effect on 26 January 1950 and lays down the framework "
                "defining political principles, government structure, and citizens' rights and duties.")

    elif "preamble" in user_input_lower:
        return ("The Preamble declares India to be a Sovereign, Socialist, Secular, Democratic Republic "
                "and aims to secure Justice, Liberty, Equality, and Fraternity for all citizens.")

    # Fundamental Rights (Articles 12–35)
    elif "fundamental rights" in user_input_lower:
        return ("Fundamental Rights are guaranteed in Part III (Articles 12–35) of the Indian Constitution. "
                "They ensure individual liberty and equality. They include:\n"
                "1️⃣ Right to Equality (Articles 14–18)\n"
                "2️⃣ Right to Freedom (Articles 19–22)\n"
                "3️⃣ Right against Exploitation (Articles 23–24)\n"
                "4️⃣ Right to Freedom of Religion (Articles 25–28)\n"
                "5️⃣ Cultural and Educational Rights (Articles 29–30)\n"
                "6️⃣ Right to Constitutional Remedies (Article 32)\n\n"
                "These rights protect citizens from arbitrary actions by the state and form the foundation of Indian democracy.")

    # ✅ Articles 1–20
    elif "article 1" in user_input_lower:
        return "Article 1: India, that is Bharat, shall be a Union of States."
    elif "article 2" in user_input_lower:
        return "Article 2: Parliament may admit new states into the Union or establish new states."
    elif "article 3" in user_input_lower:
        return "Article 3: Parliament may form new states or alter areas, boundaries, or names of existing states."
    elif "article 4" in user_input_lower:
        return "Article 4: Laws made under Articles 2 and 3 to provide for amendment of the First and Fourth Schedules."
    elif "article 5" in user_input_lower:
        return "Article 5: Citizenship at the commencement of the Constitution."
    elif "article 6" in user_input_lower:
        return "Article 6: Rights of citizenship of certain persons who have migrated to India from Pakistan."
    elif "article 7" in user_input_lower:
        return "Article 7: Rights of citizenship of certain migrants to Pakistan."
    elif "article 8" in user_input_lower:
        return "Article 8: Rights of citizenship of certain persons of Indian origin residing outside India."
    elif "article 9" in user_input_lower:
        return "Article 9: Persons voluntarily acquiring citizenship of a foreign State not to be citizens."
    elif "article 10" in user_input_lower:
        return "Article 10: Continuance of the rights of citizenship."
    elif "article 11" in user_input_lower:
        return "Article 11: Parliament to regulate the right of citizenship by law."
    elif "article 12" in user_input_lower:
        return "Article 12: Definition of the State."
    elif "article 13" in user_input_lower:
        return "Article 13: Laws inconsistent with or in derogation of Fundamental Rights to be void."
    elif "article 14" in user_input_lower:
        return "Article 14: Equality before law and equal protection of the laws."
    elif "article 15" in user_input_lower:
        return "Article 15: Prohibition of discrimination on grounds of religion, race, caste, sex, or place of birth."
    elif "article 16" in user_input_lower:
        return "Article 16: Equality of opportunity in matters of public employment."
    elif "article 17" in user_input_lower:
        return "Article 17: Abolition of untouchability."
    elif "article 18" in user_input_lower:
        return "Article 18: Abolition of titles."
    elif "article 19" in user_input_lower:
        return "Article 19: Protection of certain rights regarding freedom of speech, etc."
    elif "article 20" in user_input_lower:
        return "Article 20: Protection in respect of conviction for offences."

    # Directive Principles (Part IV)
    elif "directive principles" in user_input_lower or "dpsp" in user_input_lower:
        return ("Directive Principles of State Policy (Part IV, Articles 36–51) guide the state in making laws "
                "to establish social and economic democracy. They are non-justiciable but fundamental to governance.")

    elif "article 39" in user_input_lower:
        return "Article 39: Directs the State to ensure equal pay for equal work and adequate livelihood for citizens."
    elif "article 44" in user_input_lower:
        return "Article 44: Encourages the State to secure a Uniform Civil Code for all citizens."

    # Fundamental Duties (Part IVA)
    elif "fundamental duties" in user_input_lower:
        return ("Fundamental Duties are listed in Article 51A of the Constitution. "
                "They were added by the 42nd Amendment (1976). "
                "They include respecting the Constitution and national symbols, protecting the environment, "
                "promoting harmony, and developing scientific temper.")

    # Indian Penal Code (IPC)
    elif "ipc" in user_input_lower or "indian penal code" in user_input_lower:
        return "The Indian Penal Code (IPC), 1860, defines crimes and their punishments in India."
    elif "section 302" in user_input_lower:
        return "Section 302 IPC: Punishment for murder — death or life imprisonment."
    elif "section 420" in user_input_lower:
        return "Section 420 IPC: Cheating and dishonestly inducing delivery of property — punishable with imprisonment up to 7 years."
    elif "section 376" in user_input_lower:
        return "Section 376 IPC: Deals with the offence of rape and prescribes punishment for it."
    elif "section 498a" in user_input_lower:
        return "Section 498A IPC: Addresses cruelty by husband or his relatives toward a woman."

    # Landmark Cases
    elif "kesavananda bharati" in user_input_lower or "basic structure" in user_input_lower:
        return ("Kesavananda Bharati v. State of Kerala (1973) is a landmark Supreme Court judgment. "
                "It established the 'Basic Structure Doctrine', holding that Parliament cannot alter "
                "the fundamental framework of the Constitution — such as rule of law, separation of powers, and judicial review.")

    elif "article 370" in user_input_lower:
        return "Article 370 granted special status to Jammu & Kashmir; it was revoked on 5 August 2019."

    elif "hello" in user_input_lower or "hi" in user_input_lower:
        return "Hello! 👋 I’m Nyay AI (offline mode). How can I assist you with Indian legal or constitutional information today?"

    # Default fallback
    else:
        return ("I’m Nyay AI (offline mode). I couldn’t find an exact match for your question, "
                "but I suggest checking relevant Articles, IPC sections, or landmark cases in the Constitution of India.")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    try:
        conversation_history = request.json.get("history", [])
        last_user_message = conversation_history[-1]['content'] if conversation_history else "Hello"
        assistant_response = get_legal_response(last_user_message)
        return jsonify({"response": assistant_response})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"response": "Sorry, an error occurred."}), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

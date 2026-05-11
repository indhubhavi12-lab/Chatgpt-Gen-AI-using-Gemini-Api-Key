from google import genai
import json

# Gemini API Key
client = genai.Client(api_key="Enter your api Key")


def save_chat_output(user_text, bot_text):
    with open("chat_output.txt", "a", encoding="utf-8") as f:
        f.write("User: " + user_text + "\n")
        f.write("Bot: " + bot_text + "\n\n")


# -----------------------------
# Create sample product database
# -----------------------------
def create_products():

    products = {
        "Gaming Laptop": {
            "brand": "ASUS ROG",
            "price": "$1500",
            "features": ["RTX 4070", "16GB RAM", "1TB SSD"]
        },
        "4K TV": {
            "brand": "Samsung",
            "price": "$900",
            "features": ["55 inch", "OLED", "HDR10+"]
        }
    }

    with open("products.json", "w") as f:
        json.dump(products, f, indent=4)


# -----------------------------
# Read categories/products
# -----------------------------
def get_products_and_category():

    with open("products.json", "r") as f:
        return json.load(f)


# -----------------------------
# Extract product names
# -----------------------------
def find_category_and_product_only(user_query, categories_mapping):

    found_products = []

    for product in categories_mapping.keys():

        if product.lower() in user_query.lower():
            found_products.append(product)

    return str(found_products)


# -----------------------------
# Convert string to list
# -----------------------------
def read_string_to_list(string_data):

    try:
        return eval(string_data)
    except:
        return []


# -----------------------------
# Generate detailed info
# -----------------------------
def generate_output_string(product_list):

    with open("products.json", "r") as f:
        data = json.load(f)

    output = ""

    for item in product_list:

        if item in data:

            details = data[item]

            output += f"""
Product: {item}
Brand: {details['brand']}
Price: {details['price']}
Features: {', '.join(details['features'])}

"""

    return output


# -----------------------------
# Ask Gemini for final response
# -----------------------------
def answer_user_msg(user_query, product_info_string):

    prompt = f"""
User Question:
{user_query}

Product Information:
{product_info_string}

Provide a helpful customer service style response.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    reply = response.text
    save_chat_output(user_query, reply)

    return reply


# -----------------------------
# Evaluation Prompt
# -----------------------------
step_6_system_message_content = """
Check whether the response is factually correct and helpful.
"""


# -----------------------------
# Gemini Evaluation
# -----------------------------
def get_completion_from_messages(messages):

    prompt = ""

    for msg in messages:
        prompt += f"{msg['role']}: {msg['content']}\n"

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    reply = response.text
    save_chat_output(prompt.strip(), reply)

    return reply

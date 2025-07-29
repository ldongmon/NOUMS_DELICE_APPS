import streamlit as st
import urllib.parse

st.set_page_config(page_title="NOUMS DELICE - Commande", layout="centered")

# --- Bandeau avec logo central + petites photos à gauche et droite ---
col1, col2, col3 = st.columns([1, 2, 1])  # colonnes proportionnelles

with col1:
    st.image("poulet.jpg", width=150)  # petite image à gauche

with col2:
    st.image("logo_superdelice.png", width=300)  # logo plus grand au centre

with col3:
    st.image("samoussa.jpeg", width=150)  # petite image à droite

st.title("🍽️ NOUMS DELICE")
st.markdown("### Commandez vos spécialités maison 🔥")
st.markdown("---")

with col3:
    st.image("samoussa.jpeg", width=150)  # petite image à droite

# --- Galerie photos ---
st.markdown("---")
st.header("📸 Galerie de nos plats")

gallery = [
    ("poulet.jpg", "Poulet Épicé"),
    ("samoussa.jpeg", "Samoussa Pili-Pili"),
    ("riz.jpg", "Riz parfumé"),
    ("sauce.jpg", "Sauce Pili Pili"),
]

cols = st.columns(2)

for i, (img, caption) in enumerate(gallery):
    with cols[i % 2]:
        st.image(img, caption=caption, use_column_width=True)

# --- Menu Produits ---
st.header("🧆 Menu")

produits = {
    "Samoussa ": 1.50,
    "Poulet Épicé": 6.00,
    "Riz parfumé": 3.00,
    "Sauce pili pli(Piment)": 2.50
}

quantites = {}
total = 0

for produit, prix in produits.items():
    qty = st.number_input(f"{produit} - {prix:.2f}€", min_value=0, step=1)
    if qty > 0:
        quantites[produit] = qty
        total += prix * qty

st.markdown(f"### 💰 Total de la commande : **{total:.2f} €**")
st.markdown("---")

# --- Formulaire Client ---
st.header("🧾 Informations client")

nom = st.text_input("👤 Ton prénom et nom")
telephone = st.text_input("📱 Ton numéro de téléphone")

livraison_mode = st.radio("🚚 Mode de retrait :", ["À emporter", "Livraison"])
adresse = ""
if livraison_mode == "Livraison":
    adresse = st.text_area("📍 Adresse complète pour la livraison")
else:
    adresse = "À emporter"

# --- Génération WhatsApp ---
if nom and quantites:
    message = f"Bonjour NOUMS DELICE 👋 ! Je m'appelle {nom}.\n\nJe souhaite commander :\n"
    for produit, qty in quantites.items():
        message += f"- {qty} x {produit} = {produits[produit]*qty:.2f}€\n"
    message += f"\nTotal : {total:.2f} €\n"
    message += f"\nMode : {livraison_mode}\nAdresse : {adresse}\nTéléphone : {telephone}"

    numero_whatsapp = "33612345678"  # remplace par ton numéro sans le +
    message_url = urllib.parse.quote(message)
    lien_whatsapp = f"https://wa.me/{numero_whatsapp}?text={message_url}"

    st.markdown("---")
    st.success("✅ Ta commande est prête !")
    st.markdown(f"[📲 Envoyer la commande via WhatsApp]({lien_whatsapp})", unsafe_allow_html=True)

elif not nom:
    st.info("🟡 Remplis ton nom pour générer la commande.")
elif not quantites:
    st.info("🟡 Choisis au moins un produit.")

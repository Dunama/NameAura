import io
import os
import random
import textwrap
from flask import Flask, render_template, request, send_file, session, redirect, url_for
from PIL import Image, ImageDraw, ImageFont
    
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, template_folder='src/templates')
app.secret_key = os.environ.get("SECRET_KEY")

# dictionary of the traits
traits = {
    "Creativity": random.randint(50, 100),
    "Leadership": random.randint(60, 100),
    "Kindness": random.randint(60, 100),
    "Confidence": random.randint(50, 100),
    "Wisdom": random.randint(60, 100),
    "Intuition": random.randint(50, 100),
    "Strength": random.randint(40, 100),
    "Compassion": random.randint(60, 100),
    "Courage": random.randint(30, 100),
    "Peacefulness": random.randint(60, 100),
    "Positivity": random.randint(60, 100),
    "Determination": random.randint(60, 100),
    "Patience": random.randint(20, 100),
    "Intelligence": random.randint(30, 100),
    "Charisma": random.randint(60, 100),
    "Generosity": random.randint(60, 100),
    "Focus": random.randint(30, 100),
    "Resilience": random.randint(60, 100),
    "Spirituality": random.randint(40, 100),
    "Honesty": random.randint(10, 100)
}
# aura colors
aura_colors = {
    "Creativity": "#FF6FD8",       
    "Leadership": "#4A90E2",       
    "Kindness": "#FFB7A5",         
    "Confidence": "#F8D14A",       
    "Wisdom": "#9B59B6",           
    "Intuition": "#7F00FF",        
    "Strength": "#FF4500",         
    "Compassion": "#FF8C94",       
    "Courage": "#FF7F50",          
    "Peacefulness": "#7ED6DF",     
    "Positivity": "#F9E79F",       
    "Determination": "#C0392B",    
    "Patience": "#6DD5C4",         
    "Intelligence": "#2980B9",     
    "Charisma": "#F368E0",         
    "Generosity": "#F7DC6F",       
    "Focus": "#2ECC71",            
    "Resilience": "#8E44AD",       
    "Spirituality": "#BB8FCE",     
    "Honesty": "#00C9A7"           
}

# aura meanings
aura_meanings = [
    "Your aura radiates confidence and strength.",
    "Your energy reveals calmness and deep intuition.",
    "Your presence inspires creativity and hope.",
    "Your aura reflects leadership and purpose.",
    "Your energy shines with kindness and compassion.",
    "Your aura emits warmth and healing.",
    "Your spirit glows with unstoppable determination.",
    "Your energy carries wisdom beyond your years.",
    "Your aura sparks courage in others.",
    "Your presence brings peace wherever you go.",
    "Your energy vibrates with positivity and joy.",
    "Your aura reflects a strong and resilient heart.",
    "Your spirit radiates honesty and purity.",
    "Your aura glows with deep spiritual insight.",
    "Your energy inspires trust and loyalty.",
    "Your presence brings harmony to those around you.",
    "Your aura sparkles with imaginative power.",
    "Your spirit shines with gentle understanding.",
    "Your aura reveals inner strength hidden beneath calm.",
    "Your energy carries the light of new beginnings.",
    "Your aura pulses with fearless boldness.",
    "Your presence releases calmness into every moment.",
    "Your aura reflects a balanced and grounded soul.",
    "Your energy resonates with sharp intelligence.",
    "Your spirit glows with peaceful determination.",
    "Your aura emits an inspiring sense of purpose.",
    "Your energy radiates quiet confidence.",
    "Your aura reflects a heart full of love.",
    "Your presence is filled with creative sparks.",
    "Your aura glows with noble intentions.",
    "Your energy reveals a focused and stable mind.",
    "Your aura carries the rhythm of perseverance.",
    "Your spirit vibrates with generosity and care.",
    "Your aura emits a brave and confident spirit.",
    "Your presence feels refreshing and uplifting.",
    "Your energy shows deep emotional strength.",
    "Your aura reveals a gentle yet powerful heart.",
    "Your spirit inspires growth and transformation.",
    "Your aura carries the glow of pure potential.",
    "Your energy shines with purpose and clarity.",
    "Your aura reflects a visionary and open mind.",
    "Your spirit radiates a calming and steady force.",
    "Your presence brings inspiration to those around you.",
    "Your aura glows with emotional intelligence and grace.",
    "Your energy carries the spark of transformation.",
    "Your spirit shines with timeless wisdom.",
    "Your aura radiates hope and pure intention.",
    "Your presence reflects a soul full of depth and clarity.",
    "Your energy vibrates with quiet yet powerful influence."
]


@app.route('/')
def homePage():
    '''to display the home page'''
    return render_template('homePage.html')

@app.route('/aura', methods=['POST'])
def generate_aura():
    """Generate aura data from form submit and include trait colors."""
    name = (request.form.get('name') or '').strip()
    if not name:
        return render_template('homePage.html', error="Please enter a valid name.")

    # Generate fresh random trait scores each request
    generated_traits = {trait: random.randint(60, 100) for trait in traits.keys()}
    # Pick 3 random traits to highlight
    highlighted = random.sample(list(generated_traits.items()), 3)
    aura_meaning = random.choice(aura_meanings)

    # Enrich with colors for template rendering
    enriched_traits = [
        {
            "trait": trait,
            "score": score,
            "color": aura_colors.get(trait, "#ffffff"),
        }
        for trait, score in highlighted
        # we added this comment to track github modifications
    ]
    format_name=name.upper()
    session['last_result'] = {
        "name": format_name,
        "traits": enriched_traits,
        "aura_meaning": aura_meaning,
    }

    return render_template('aura.html', name=format_name, traits=enriched_traits, aura_meaning=aura_meaning)



if __name__ == '__main__':
    app.run(debug=False)

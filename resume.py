from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import black, darkblue

def generate_google_resume():
    # FIX: Changed path to just the filename so it saves in your current folder
    doc = SimpleDocTemplate("Abdul_Wahab_Khan_Google_Resume.pdf", pagesize=LETTER,
                            rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    styles = getSampleStyleSheet()
    
    # Custom Styles
    name_style = ParagraphStyle('Name', parent=styles['Heading1'], fontSize=20, alignment=1, spaceAfter=5)
    contact_style = ParagraphStyle('Contact', parent=styles['Normal'], fontSize=9, alignment=1, spaceAfter=15)
    header_style = ParagraphStyle('SectionHeader', parent=styles['Heading2'], fontSize=11, spaceBefore=10, spaceAfter=2,
                                  textColor=darkblue, textTransform='uppercase')
    job_title_style = ParagraphStyle('JobTitle', parent=styles['Heading3'], fontSize=10, spaceBefore=4, spaceAfter=1)
    bullet_style = ParagraphStyle('Bullet', parent=styles['Normal'], fontSize=10, leading=12, leftIndent=15, bulletIndent=5)
    
    story = []
    
    # --- Header ---
    story.append(Paragraph("ABDUL WAHAB KHAN", name_style))
    contact_info = (
        "Karachi, Pakistan | +92 342-8320022<br/>"
        "<a href='mailto:absurw@gmail.com'>absurw@gmail.com</a> | "
        "<a href='https://abdulwahabkhan-portfolio.vercel.app/'>Portfolio</a> | "
        "<a href='https://github.com/abdulwahabahmedkhanyusufzai'>GitHub</a> | "
        "<a href='https://linkedin.com/in/awahab1567'>LinkedIn</a>"
    )
    story.append(Paragraph(contact_info, contact_style))
    story.append(HRFlowable(width="100%", thickness=1, color=black))
    
    # --- Education ---
    story.append(Paragraph("EDUCATION", header_style))
    story.append(Paragraph("<b>Virtual University of Pakistan</b> | BS Computer Science (July 2025 – Present)", job_title_style))
    story.append(Paragraph("Focus: Data Structures & Algorithms, Calculus, Linear Algebra.", bullet_style, bulletText="•"))
    story.append(Paragraph("Plan: Pursuing Master’s in CS at Georgia Tech post-graduation.", bullet_style, bulletText="•"))
    story.append(Paragraph("<b>Karachi University</b> | B.Com (Banking & Finance) (Jan 2022 – Jan 2024)", job_title_style))

    # --- Technical Skills ---
    story.append(Paragraph("TECHNICAL SKILLS", header_style))
    skills = [
        "<b>Languages:</b> C++, Python, JavaScript (ES6+), TypeScript, Java, SQL",
        "<b>AI/ML:</b> TensorFlow, PyTorch, NumPy, Pandas, Scikit-learn, Vertex AI",
        "<b>Web Engineering:</b> React.js, Next.js, Node.js, Express, MongoDB, Google Cloud Platform (GCP)",
        "<b>Core:</b> Data Structures & Algorithms, Distributed Systems, OOP, System Design"
    ]
    for skill in skills:
        story.append(Paragraph(skill, bullet_style, bulletText="•"))

    # --- Experience ---
    story.append(Paragraph("EXPERIENCE", header_style))
    
    story.append(Paragraph("<b>QF Network</b> | MERN Stack Developer (Karachi | March 2025 – Present)", job_title_style))
    story.append(Paragraph("Architected a SaaS platform for AI-powered e-commerce, enabling one-click store generation for 500+ users.", bullet_style, bulletText="•"))
    story.append(Paragraph("Reduced merchant onboarding time by 60% by engineering an automated theme deployment pipeline using React and Node.js.", bullet_style, bulletText="•"))
    
    story.append(Paragraph("<b>Fiverr</b> | Full-Stack Developer (Remote | Feb 2025 – Present)", job_title_style))
    story.append(Paragraph("Engineered 'Cyrano,' a smart itinerary planner, integrating Google Maps API and GPT-4 for dynamic route optimization.", bullet_style, bulletText="•"))
    story.append(Paragraph("Increased trip planning accuracy by 50% by finetuning prompt engineering strategies for location-based recommendations.", bullet_style, bulletText="•"))

    # --- Projects ---
    story.append(Paragraph("PROJECTS (AI & SYSTEMS FOCUS)", header_style))
    
    story.append(Paragraph("<b>Real-Time Audio Translation Model</b> | Python, PyTorch, Deep Learning", job_title_style))
    story.append(Paragraph("Developing an end-to-end audio-to-audio voice translation model aiming to rival ElevenLabs in latency.", bullet_style, bulletText="•"))
    
    story.append(Paragraph("<b>Scalable Video Streaming Engine</b> | MERN, Google Cloud, Vercel", job_title_style))
    story.append(Paragraph("Built a distributed video streaming service handling 5,000+ minutes of content with 99.9% uptime on Vercel.", bullet_style, bulletText="•"))
    story.append(Paragraph("Improved video playback performance by 40% through lazy loading and chunked data streaming.", bullet_style, bulletText="•"))
    
    story.append(Paragraph("<b>Kaggle Competition: Protein Function Prediction</b> | Python, Bio-informatics", job_title_style))
    story.append(Paragraph("Ranked in top percentile for 'CAFA 6 Protein Function Prediction' by utilizing ensemble learning techniques.", bullet_style, bulletText="•"))
    
    # --- Achievements ---
    story.append(Paragraph("ACHIEVEMENTS", header_style))
    story.append(Paragraph("<b>LeetCode:</b> Solved 109+ DSA problems, focusing on Graph Theory and Dynamic Programming.", bullet_style, bulletText="•"))
    story.append(Paragraph("<b>Open Source:</b> Active contributor to web application repositories on GitHub.", bullet_style, bulletText="•"))

    # Build PDF
    doc.build(story)
    print("Resume generated successfully: Abdul_Wahab_Khan_Google_Resume.pdf")

if __name__ == "__main__":
    generate_google_resume()
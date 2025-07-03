from fpdf import FPDF

def student_data():
    student = {}
    student["name"] = input("Enter name: ")
    student["email"] = input("Enter email: ")
    student["phone"] = input("Enter phone: ")
    student["address"] = input("Enter address: ")
    student["education"] = input("Enter education details: ")
    student["skills"] = input("Enter skills (comma separated): ")
    student["experience"] = input("Enter work experience: ")
    return student
def create_resume_pdf(student):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, txt=student["name"], ln=True, align="C")

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Email: {student['email']}", ln=True)
    pdf.cell(200, 10, txt=f"Phone: {student['phone']}", ln=True)
    pdf.cell(200, 10, txt=f"Address: {student['address']}", ln=True)

    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, txt="Education", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, student["skills"])

    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, txt="Experience", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, student["experience"])

    pdf.output("resume.pdf")

if __name__ == "__main__":
    student = student_data()
import streamlit as st

# Header / Banner
st.markdown("""
    <div style='background-color:lightblue; padding:10px; text-align:center'>
        <h1 style='color:black;'>Job Hunt</h1>
        <p style='color:darkblue;'>Find your dream job and apply easily!</p>
    </div>
    """, unsafe_allow_html=True)

# Sidebar for Job Filters
st.sidebar.header("Search Jobs")
job_title = st.sidebar.text_input("Job Title")
location = st.sidebar.text_input("Location")
job_type = st.sidebar.selectbox("Job Type", ["All", "Full-time", "Part-time", "Internship"])

# Sidebar - Job Application Form
st.sidebar.header("Apply to Job")
selected_job = st.sidebar.selectbox("Select Job", ["Data Scientist", "Backend Developer", "Marketing Manager"])
applicant_name = st.sidebar.text_input("Full Name")
applicant_email = st.sidebar.text_input("Email")
resume = st.sidebar.file_uploader("Upload Resume", type=["pdf", "docx"])

if st.sidebar.button("Submit Application"):
    if applicant_name and applicant_email and resume:
        st.sidebar.success(f"Application submitted for {selected_job} by {applicant_name}")
    else:
        st.sidebar.error("Please fill out all fields.")

# Sample Job Listings Data
job_listings = [
    {"title": "Data Scientist", "company": "Tech Corp", "location": "Remote", "job_type": "Full-time",
     "description": "Build and maintain ML models."},
    {"title": "Backend Developer", "company": "DevWorks", "location": "New York", "job_type": "Part-time",
     "description": "Develop and maintain backend services."},
    {"title": "Marketing Manager", "company": "BrandMasters", "location": "San Francisco", "job_type": "Full-time",
     "description": "Lead the marketing strategy for the company."}
]

# Filter Job Listings
filtered_jobs = [job for job in job_listings if
                 (job_title.lower() in job['title'].lower()) and
                 (location.lower() in job['location'].lower()) and
                 (job_type == "All" or job_type == job['job_type'])]

# Display Job Listings
st.subheader("Available Jobs")
for job in filtered_jobs:
    st.markdown(f"**{job['title']} at {job['company']}**")
    st.markdown(f"*Location: {job['location']}*")
    st.markdown(f"*Job Type: {job['job_type']}*")
    st.markdown(f"Description: {job['description']}")
    st.markdown(f"[Apply Now](https://www.example.com/apply/{job['title'].replace(' ', '_')})")
    st.markdown("---")

# Footer
st.markdown("""
    <div style='background-color:lightgrey; padding:10px; text-align:center'>
        <p>© 2024 Job Hunt Inc. | <a href='#'>Contact Us</a> | <a href='#'>Privacy Policy</a></p>
    </div>
    """, unsafe_allow_html=True)

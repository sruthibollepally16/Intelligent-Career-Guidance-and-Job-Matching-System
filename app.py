import streamlit as st

# ---------------- PAGE CONFIGURATION ----------------
st.set_page_config(
    page_title="Career Guidance System",
    page_icon="🎯",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main-title {
    font-size: 40px;
    font-weight: bold;
    text-align: center;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: gray;
}

.card {
    padding: 20px;
    border-radius: 12px;
    background-color: #f5f5f5;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown(
    '<div class="main-title">🎯 Intelligent Career Guidance and Job Matching System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Find the best career path and job opportunities based on your skills and interests.</div>',
    unsafe_allow_html=True
)

st.write("")

# ---------------- SIDEBAR ----------------
st.sidebar.title("👤 Student Profile")

name = st.sidebar.text_input("Student Name")

education = st.sidebar.selectbox(
    "Education",
    [
        "B.Tech",
        "B.Sc",
        "BCA",
        "MCA",
        "MBA",
        "Other"
    ]
)

branch = st.sidebar.selectbox(
    "Branch",
    [
        "CSE",
        "ECE",
        "EEE",
        "IT",
        "Mechanical",
        "Civil",
        "Other"
    ]
)

skills = st.sidebar.multiselect(
    "💻 Select Your Skills",
    [
        "Python",
        "Java",
        "C",
        "SQL",
        "HTML/CSS",
        "JavaScript",
        "Machine Learning",
        "Data Analysis",
        "Communication",
        "Problem Solving"
    ]
)

interests = st.sidebar.multiselect(
    "❤️ Select Your Interests",
    [
        "Artificial Intelligence",
        "Web Development",
        "Data Science",
        "Cyber Security",
        "Software Development",
        "Cloud Computing",
        "Business"
    ]
)

# ---------------- CAREER DATABASE ----------------
careers = {

    "Artificial Intelligence": {
        "career": "AI / Machine Learning Engineer",
        "skills": [
            "Python",
            "Machine Learning",
            "Problem Solving"
        ],
        "jobs": [
            "AI Intern",
            "Machine Learning Intern",
            "AI Engineer"
        ]
    },

    "Web Development": {
        "career": "Web Developer",
        "skills": [
            "HTML/CSS",
            "JavaScript",
            "Python"
        ],
        "jobs": [
            "Frontend Developer",
            "Backend Developer",
            "Web Developer"
        ]
    },

    "Data Science": {
        "career": "Data Scientist / Data Analyst",
        "skills": [
            "Python",
            "SQL",
            "Data Analysis"
        ],
        "jobs": [
            "Data Analyst",
            "Junior Data Scientist",
            "Data Science Intern"
        ]
    },

    "Cyber Security": {
        "career": "Cyber Security Analyst",
        "skills": [
            "C",
            "Python",
            "Problem Solving"
        ],
        "jobs": [
            "Security Analyst",
            "Cyber Security Intern",
            "Security Engineer"
        ]
    },

    "Software Development": {
        "career": "Software Developer",
        "skills": [
            "Python",
            "Java",
            "SQL",
            "Problem Solving"
        ],
        "jobs": [
            "Software Developer",
            "Java Developer",
            "Python Developer"
        ]
    },

    "Cloud Computing": {
        "career": "Cloud Engineer",
        "skills": [
            "Python",
            "Problem Solving"
        ],
        "jobs": [
            "Cloud Intern",
            "Cloud Engineer",
            "DevOps Intern"
        ]
    },

    "Business": {
        "career": "Business Analyst",
        "skills": [
            "SQL",
            "Communication",
            "Data Analysis"
        ],
        "jobs": [
            "Business Analyst",
            "Management Trainee",
            "Business Analyst Intern"
        ]
    }
}

# ---------------- FIND CAREER BUTTON ----------------
if st.button("🔍 Find My Career", use_container_width=True):

    # -------- VALIDATION --------
    if name.strip() == "":
        st.error("⚠️ Please enter your name.")

    elif len(skills) == 0:
        st.error("⚠️ Please select at least one skill.")

    elif len(interests) == 0:
        st.error("⚠️ Please select at least one interest.")

    else:

        st.success(
            f"Welcome {name}! Your personalized career recommendations are ready."
        )

        # -------- CAREER MATCHING --------
        results = []

        for interest in interests:

            data = careers[interest]

            required_skills = set(data["skills"])
            student_skills = set(skills)

            matching_skills = required_skills.intersection(
                student_skills
            )

            missing_skills = required_skills.difference(
                student_skills
            )

            score = (
                len(matching_skills)
                / len(required_skills)
                * 100
            )

            results.append({
                "career": data["career"],
                "score": score,
                "required_skills": data["skills"],
                "matching_skills": list(matching_skills),
                "missing_skills": list(missing_skills),
                "jobs": data["jobs"]
            })

        # -------- SORT RESULTS --------
        results.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        # -------- BEST CAREER --------
        best = results[0]

        st.divider()

        st.header("🏆 Your Best Career Match")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Recommended Career",
                best["career"]
            )

        with col2:
            st.metric(
                "Match Score",
                f"{best['score']:.0f}%"
            )

        with col3:
            st.metric(
                "Education",
                education
            )

        st.progress(
            int(best["score"])
        )

        st.write(
            f"Based on your selected skills and interests, "
            f"**{best['career']}** is your strongest career match."
        )

        # -------- MATCHING SKILLS --------
        st.divider()

        st.header("✅ Matching Skills")

        if best["matching_skills"]:

            for skill in best["matching_skills"]:
                st.success(f"✓ {skill}")

        else:
            st.info("No matching skills found.")

        # -------- SKILL GAP --------
        st.header("📚 Skills You Need to Improve")

        if best["missing_skills"]:

            for skill in best["missing_skills"]:
                st.warning(f"📌 Learn: {skill}")

        else:

            st.success(
                "🎉 You already have all the required skills!"
            )

        # -------- JOB RECOMMENDATIONS --------
        st.divider()

        st.header("💼 Recommended Job Roles")

        job_columns = st.columns(len(best["jobs"]))

        for i, job in enumerate(best["jobs"]):

            with job_columns[i]:
                st.info(f"**{job}**")

        # -------- OTHER CAREERS --------
        st.divider()

        st.header("📊 Other Career Matches")

        for result in results:

            col1, col2 = st.columns([4, 1])

            with col1:
                st.write(
                    f"**{result['career']}**"
                )

                st.progress(
                    int(result["score"])
                )

            with col2:
                st.write(
                    f"**{result['score']:.0f}%**"
                )

        # -------- CAREER GUIDANCE --------
        st.divider()

        st.header("🤖 Career Guidance")

        if best["score"] >= 70:

            st.success(
                "🌟 Excellent career match! "
                "You already have most of the required skills. "
                "Focus on real-world projects, internships, "
                "certifications and interview preparation."
            )

        elif best["score"] >= 40:

            st.info(
                "👍 You have a good foundation for this career. "
                "Work on the missing skills and build 2–3 projects "
                "to improve your career opportunities."
            )

        else:

            st.warning(
                "📖 You are at the beginning of this career path. "
                "Start learning the recommended skills, practice "
                "regularly and build beginner-level projects."
            )

        # -------- STUDENT SUMMARY --------
        st.divider()

        st.header("📋 Student Profile Summary")

        st.write(f"**Name:** {name}")
        st.write(f"**Education:** {education}")
        st.write(f"**Branch:** {branch}")
        st.write(
            f"**Skills:** {', '.join(skills)}"
        )
        st.write(
            f"**Interests:** {', '.join(interests)}"
        )

else:

    st.info(
        "👈 Enter your details in the sidebar and click "
        "**🔍 Find My Career** to get recommendations."
    )
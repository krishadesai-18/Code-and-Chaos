from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

ROLE_SKILLS = {
    "health_informatics_analyst": [
        "SQL", "EHR", "FHIR", "HL7", "Data Analytics", "Healthcare Compliance"
    ],
    "healthcare_data_analyst": [
        "Python", "SQL", "Data Visualization", "Healthcare Data", "Statistics"
    ],
    "medical_ai_engineer": [
        "Python", "Machine Learning", "Medical Imaging", "AI Ethics", "HIPAA"
    ]
}

LEVEL_WEIGHT = {
    "Beginner": 0.4,
    "Intermediate": 0.7,
    "Advanced": 1.0
}

class Skill(BaseModel):
    name: str
    level: str

class AnalyzeRequest(BaseModel):
    role: str
    skills: List[Skill]

@router.post("/analyze")
def analyze_skills(data: AnalyzeRequest):
    required_skills = ROLE_SKILLS.get(data.role, [])
    user_skills = {s.name: s.level for s in data.skills}

    matched = [s for s in required_skills if s in user_skills]
    missing = [s for s in required_skills if s not in user_skills]

    score = sum(LEVEL_WEIGHT.get(user_skills[s], 0) for s in matched)
    readiness = int((score / len(required_skills)) * 100) if required_skills else 0

    return {
        "matched": matched,
        "missing": missing,
        "required": required_skills,
        "readiness": readiness
    }

@router.post("/recommend-courses")
def recommend_courses(data: AnalyzeRequest):
    required_skills = ROLE_SKILLS.get(data.role, [])
    user_skills = {s.name: s.level for s in data.skills}
    
    missing_skills = [s for s in required_skills if s not in user_skills]
    
    from recommendations import get_course_recommendations
    courses = get_course_recommendations(missing_skills, data.role)
    
    return {
        "missing_skills": missing_skills,
        "recommended_courses": courses
    }

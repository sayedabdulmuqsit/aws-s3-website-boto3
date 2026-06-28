# ☁️ AWS S3 Static Website — boto3 Automated

![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![S3](https://img.shields.io/badge/Amazon%20S3-569A31?style=for-the-badge&logo=amazons3&logoColor=white)

> Fully automated AWS S3 static website deployment using Python boto3 — no manual console clicks required.

🌐 **Live Demo:** [View Portfolio](http://muqsit-portfolio-site.s3-website.eu-north-1.amazonaws.com)

---

## 📌 What This Project Does

This Python script automatically:
1. Creates an S3 bucket on AWS
2. Uploads the HTML portfolio file
3. Removes public access block
4. Sets a bucket policy for public read access
5. Enables static website hosting
6. Outputs the live website URL

---

## 🛠️ Tech Stack

| Technology | Usage |
|------------|-------|
| Python 3 | Scripting |
| boto3 | AWS SDK for Python |
| AWS S3 | Static website hosting |
| IAM | Bucket policy configuration |
| HTML/CSS | Portfolio frontend |

---

## 📁 Project Structure

```
aws-s3-website-boto3/
├── s3_website.py      # Main automation script
└── index.html         # Portfolio website
```

---

## ⚙️ How to Run

**Prerequisites:**
- Python 3 installed
- boto3 installed (`pip install boto3`)
- AWS CLI configured (`aws configure`)

**Steps:**
```bash
git clone https://github.com/sayedabdulmuqsit/aws-s3-website-boto3
cd aws-s3-website-boto3
pip install boto3
python s3_website.py
```

---

## 🔑 Key Concepts Demonstrated

- **boto3** — AWS SDK for Python
- **S3 Bucket Policy** — IAM-based public access control
- **Static Website Hosting** — S3 as a web server
- **Infrastructure as Code** — No manual console clicks
- **Cloud Automation** — Repeatable, scalable deployment

---

## 👨‍💻 Author

**Abdul Muqsit Sayed**  
CSE (AI/ML) | M.H. Saboo Siddik College of Engineering, Mumbai  
[![Portfolio](https://img.shields.io/badge/Portfolio-Live-FF9900?style=flat)](http://muqsit-portfolio-site.s3-website.eu-north-1.amazonaws.com)

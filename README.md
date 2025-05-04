- **problems/**: 각 문제의 마크다운 파일이 위치
- **questions/**: 각 문제별 학생 질문 마크다운 파일과 질문 포맷 예시
- **dataset/**: DPO 학습용 reject/chosen 쌍이 저장된 답변 파일
- **make_*.py**: 데이터 생성 및 가공 파이썬 스크립트
- **verify_*.py**: 데이터 검증 및 자동 수정 파이썬 스크립트
- **task.md**: 프로젝트 작업 및 설명 문서(그냥 메모장...)
  
📁 DPO_Fine_Tuning/
├── .env
├── .gitignore
├── make_dataset.py
├── make_problem.py
├── make_question.py
├── task.md
├── utils.sh
├── verify_dataset.py
├── verify_question.py
│
├── 📁 dataset/ (각 문제마다 예상되는 질문들에 대한 대답(reject, chosen))
│   ├── 📁 problem_1/
│   │   ├── answer_1.md
│   │   ├── answer_2.md
│   │   ├── ...
│   │   └── answer_20.md
│   ├── 📁 problem_2/
│   │   └── answer_1.md ~ answer_20.md (생략)
│   ├── 📁 problem_3/
│   ├── 📁 problem_4/
│   ├── 📁 problem_5/
│   ├── 📁 problem_6/
│   ├── 📁 problem_7/
│   └── 📁 problem_8/
│
├── 📁 dpo/ (가상환경)
│
├── 📁 problems/ (임의로 설정한 문제들)
│   ├── problem_1.md
│   ├── problem_2.md
│   ├── ...
│   └── problem_8.md
│
├── 📁 questions/ (각 문제에 대해 예상되는 질문들)
│   ├── 📁 problem_1/
│   │   ├── question_1.md
│   │   ├── question_2.md
│   │   ├── ...
│   │   └── question_20.md
│   ├── 📁 problem_2/
│   │   └── question_1.md ~ question_20.md (생략)
│   ├── 📁 problem_3/
│   ├── 📁 problem_4/
│   ├── 📁 problem_5/
│   ├── 📁 problem_6/
│   ├── 📁 problem_7/
│   └── 📁 problem_8/
│
└── question_format.md

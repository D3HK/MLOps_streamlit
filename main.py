import streamlit as st
import streamlit.components.v1 as components


def show_introduction():
    st.title("Accident Severity Prediction Pipeline")

    st.image("images/123.png", use_container_width=True)

    st.subheader("Intro")
    st.write(
        """
        Machine Learning Operations (MLOps) is important for successfully deploying and 
        maintaining machine learning models in real-world environments. It connects data science and IT operations, 
        ensuring models are developed efficiently and run smoothly at scale. 
        MLOps provides a framework for continuous integration and delivery (CI/CD), 
        monitoring, and versioning of models, helping organizations reduce risks, improve teamwork, 
        and streamline processes. By implementing MLOps, businesses can deploy models faster, 
        enhance performance, and achieve more consistent results, leading to better data-driven decision-making.
        """
    )

    st.markdown("---")

    st.subheader("Project Overview")
    st.write(
        "This MLOps project is based on predicting crash severity in France using historical crash data."
        "The project focuses on building a complete **MLOps pipeline** for deploying and managing a "
        "pre-trained machine learning model in a production environment. Unlike traditional ML projects, "
        "I did not develop the model from scratch but instead integrated an existing model to emphasize:\n\n"

        "1. **Industrialization** of ML models through reproducible pipelines.\n"
        "2. **Automation** of deployment, scaling, and monitoring.\n"
        "3. **Reliability** and scalability in production.\n\n"
    )


def show_phase_1():
    st.title("Data & Model Foundations")
    st.image("images/data.png", use_container_width=True)

    st.write(
        "The project utilizes an open-source GitHub repository as its foundation. "
        "Initial work involved data processing and fine-tuning of the provided model architecture, "
        "with results successfully integrated into the MLOps pipeline for production deployment.\n\n"

        "Link to a repository: https://github.com/DataScientest-Studio/Template_MLOps_accidents"
    )
    st.markdown("---")

    st.subheader("FastAPI: REST API for predictions")
    st.write(
        "The resulting model was packaged as a REST API using FastAPI, "
        "enabling seamless integration with other system components. "
        "Comprehensive testing validated both the API endpoints and model predictions, "
        "ensuring reliability before production deployment."
    )
    st.image("images/fastapi_swagger_1.jpg", use_container_width=True)

    st.markdown(
        """
        ### Test data
            curl -X POST "http://<your_host_ip>:5000/predict" -H "Content-Type: application/json" -d 
            '{"features": [10, 3, 1, 0.0, 2021, 60, 2, 1, 1, 3, 2, 1, 1, 50, 7, 12, 5, 77, 77317, 2, 1, 0, 6, 
            48.60, 2.89, 17, 2, 1]}'
        """
    )

    st.image("images/fastapi_swagger_2.jpg", use_container_width=True)


def show_phase_2():
    st.title("Tracking & Versioning")
    st.image("images/compass.png", use_container_width=True)
    st.write(
        """
        Tracking and versioning are essential for managing the lifecycle of ML experiments, 
        ensuring reproducibility, and enabling collaboration. They help log parameters, metrics, 
        and artifacts while maintaining a history of changes to data, code, and models.  
        """
    )

    st.subheader("MLflow: Experiment tracking")
    st.write(
        """
        MLflow is an open-source platform for managing the machine learning lifecycle.
        MLflow solves the chaos of model versioning and lets teams collaborate on ML development.
        """
    )

    st.image("images/mlflow_ui_1.jpg", caption="The list of Experiments", use_container_width=True)
    st.image("images/mlflow_ui_2.jpg", caption="Model metrics", use_container_width=True)

    st.markdown("---")

    st.subheader("DVC: Data version control")
    st.write(
        """
        DVC (Data Version Control) helps version datasets, track changes, 
        and reproduce ML pipelines reliably - keeping your experiments organized and your team in sync.
        """
    )

    st.image("images/dvc_pipeline_3.jpg", caption="It's work!", use_container_width=True)
    st.image("images/dvc_pipeline_4.jpg", caption="DVC Pipeline Dependency Graph", use_container_width=True)
    st.write(
        """
        ### **Dependency Graph Explanation**  
        **`prepare`** → **`train`** → **`evaluate`**

        1. **`prepare`**:  
           - Preprocessing stage (raw data → `data/raw`).  
           - Output: Processed data (e.g., `data/preprocessed/X_train.csv`, `y_train.csv`).  

        2. **`train`**:  
           - Model training stage (uses processed data from `prepare`).  
           - Output: Trained model (e.g., `models/trained_model.joblib`).  

        3. **`evaluate`**:  
           - Generates predictions on test data.  
           - Output: Logs to MLflow `test_accuracy`.    
        """
    )

    st.markdown("---")

    st.subheader("Docker: Containerized services")
    st.write(
        """
        Docker standardizes environments to ensure reproducibility and scalability of ML solutions. 
        Containers package code, dependencies, and models into portable units, 
        guaranteeing identical performance across all stages - from experiments to production.
        """
    )

    st.image("images/docker_workflow.png", use_container_width=True)

    st.subheader("Current Progress")
    st.write("A Docker container has been built during the development phase of our project.")
    st.image("images/docker_create_1.jpg", use_container_width=True)
    st.markdown("---")
    st.image("images/docker_create_2.jpg", use_container_width=True)


def show_phase_3():
    st.title("Orchestration & CI/CD")
    st.image("images/conductor.png", use_container_width=True)

    st.write(
        """
        Production Orchestration is essential for managing the lifecycle of applications in a production environment. 
        It automates the deployment, scaling, and monitoring of services, 
        ensuring that applications run smoothly and reliably. By coordinating various processes and tools, 
        production orchestration helps teams achieve faster release cycles and maintain high availability 
        and performance of their applications.
        """
    )

    st.subheader("Kubernetes: Scalable deployment")
    st.write(
        """
        Currently FastAPI service is normally deployed in Kubernetes 
        (deployment READY, pods are running, service is available via NodePort).
        """
    )
    st.image("images/kubernetes_cluster_wide.jpg", use_container_width=True)
    st.image("images/kubernetes_mlflow.jpg", use_container_width=True)
    st.image("images/kubernetes_grafana.jpg", use_container_width=True)

    st.subheader("Kubernetes Architecture")
    st.image("images/kubernetes_architecture.png", use_container_width=True)

    st.markdown("---")

    st.subheader("Jenkins: CI/CD pipelines")
    st.write(
        """
        In my project, I used Jenkins to automate CI/CD processes, 
        which greatly simplified the deployment and testing of machine learning models. 
        """
    )
    st.image("images/jenkins_success.jpg", use_container_width=True)
    st.markdown(
        """
        ### Pipeline Stages: [GitHub] → [Jenkins] → [Train] → [Save]    
         
        1. **Checkout SCM**  
           - Clones the Git repo.  
        
        2. **Setup**  
           - Creates Python virtual environment (`venv`).  
           - Installs dependencies (`pandas`, `scikit-learn`, `imbalanced-learn`, etc.).  
        
        3. **Train Model**  
           - Runs `train_model.py` → **"Model trained and saved successfully."**  
        
        4. **Archive Artifacts**  
           - Saves outputs (e.g., trained model).  
        """
    )

    st.markdown("---")

    st.subheader("Jenkins Pipeline")
    st.code(
        """
        pipeline {
            agent any
        
            stages {
                stage('Checkout') {
                    steps {
                        checkout scm
                    }
                }
        
                stage('Setup') {
                    steps {
                        sh '''
                            python3 -m venv venv
                            . venv/bin/activate
                            pip install -r requirements.txt
                        '''
                    }
                }
        
                stage('Train') {
                    steps {
                        sh '''
                            . venv/bin/activate
                            python src/models/train_model.py
                            ls -la models/  # Проверка содержимого
                        '''
                    }
                }
        
                stage('Archive Model') {
                    steps {
                        archiveArtifacts artifacts: 'src/models/*.joblib', fingerprint: true
                    }
                }
            }
        }
        """,
        language='groovy'
    )


def show_phase_4():
    st.title("Monitoring")
    st.image("images/dashboard.png", use_container_width=True)

    st.write(
        """
        Prometheus and Grafana are essential tools for monitoring and visualizing the performance 
        and health of applications and infrastructure. Prometheus efficiently collects and stores metrics data, 
        while Grafana offers powerful visualization capabilities to create interactive dashboards. 
        Together, they enable real-time monitoring, facilitating quick troubleshooting and performance assessment. 
        \n\n
        On the other hand, Evidently focuses specifically on monitoring machine learning models in production, 
        helping teams detect model drift, biases, and performance issues over time. 
        By providing insights into model behavior, Evidently ensures that models remain accurate and reliable, 
        allowing for proactive adjustments to improve overall performance.
        """
    )

    st.subheader("Prometheus")
    st.image("images/prometheus.jpg", use_container_width=True)

    st.subheader("Grafana: Real-time dashboards")
    st.write(
        """
        Grafana visualizes the data collected by Prometheus in the form of interactive dashboards and graphs. 
        This allows us to track important metrics in real time.
        """
    )
    st.image("images/grafana.jpg", use_container_width=True)

    st.subheader("To Docker Container")
    st.image("images/docker_create_4.jpg", use_container_width=True)

    st.markdown("---")

    st.subheader("Evidently: Data drift detection")
    st.write(
        """
        The current analysis indicates that drift has been detected for 0.00% of features (0 out of 28), 
        meaning that the model's input features remain consistent with their expected distributions. 
        Additionally, since dataset drift is not detected, it suggests that the underlying data 
        has not significantly changed, allowing for reliable model performance under current conditions.
        """
    )
    # --- вставка HTML ---
    with open("images/drift_report.html", "r", encoding="utf-8") as f:
        html_content = f.read()

    components.html(
        html_content,
        height=600,
        scrolling=True
    )


def show_documentation():
    st.title("Technical Documentation: MLOps Roadmap")
    st.markdown("""
        This project demonstrates how to design, deploy, and maintain a machine learning pipeline for predicting **road accident severity in France** using a structured MLOps approach.
    
        ## Project Phases and Technology Stack
    
        #### 🧱 Phase 1: Foundations & Containerization   
            - Defined project goals and KPIs  
            - Set up reproducible environment using GitHub and local scripts  
            - Collected and preprocessed crash data  
            - Used a pre-trained baseline ML model  
            - Built a basic inference API  
            Tools: GitHub, Python scripts, FastAPI  
    
        ---
    
        #### 🧪 Phase 2: Microservices, Tracking & Versioning  
            - Enabled experiment tracking with MLflow 
            - Implemented data and model versioning using DVC 
            - Modularized the application into FastAPI microservices  
            - Containerized services using Docker 
            Tools: MLflow, DVC, FastAPI, Docker  
    
        ---
    
        #### 🔁 Phase 3: Orchestration & Deployment  
            - Built an end-to-end orchestrated pipeline with ZenML 
            - Designed CI pipeline using Jenkins 
            - Optimized and secured the API for production  
            - Added scalability support via Docker & Kubernetes 
            Tools: ZenML, Jenkins, FastAPI, Docker, Kubernetes  
    
        ---
    
        #### 📊 Phase 4: Monitoring & Maintenance   
            - Monitored model and API with Prometheus & Grafana 
            - Implemented drift detection using Evidently 
            - Automated updates for model and components  
            - Finalized full technical documentation for delivery  
            Tools: Prometheus, Grafana, Evidently, Jenkins  
    
        ---
    
        ## Final Objective:
        Deliver a production-ready, modular, and scalable MLOps pipeline that ensures:
            - Model reproducibility and traceability  
            - Deployment automation  
            - Monitoring and reliability  
            - Clear documentation for future maintenance
    
        ### 🔗 Model Source:
        [GitHub Template Repository](https://github.com/DataScientest-Studio/Template_MLOps_accidents)
    """
                )


def show_conclusion():
    st.title("Conclusion")
    st.image("images/rocket.png", use_container_width=True)

    st.write(
        """
        In conclusion, I can say that I have achieved the goals of my project and ensured 
        the stable operation of the machine learning and monitoring systems. 
        A clear approach to analyzing and controlling model performance allowed me to identify possible issues, 
        which improved reliability and expanded my skills in data analytics.\n\n

        One of the main achievements is that there was no detected data drift, 
        showing the stability and quality of the models used. A proper approach to monitoring and support 
        will help ensure the project's continued success.\n\n
        
        Now, I plan to focus on improving my skills and abilities in this field, 
        adapting to changes and new requirements. The main goal is to maintain a high level of quality 
        and reliability in achieving the set tasks.
        """
    )


def main():
    st.set_page_config(page_title="MLOps Accidents Project", page_icon="🚙", layout="wide")

    page = st.sidebar.radio(
        "Main menu", [
            "Introduction",
            "Phase 1",
            "Phase 2",
            "Phase 3",
            "Phase 4",
            "Documentation",
            "Conclusion"
        ]
    )

    if page == "Introduction":
        show_introduction()
    elif page == "Phase 1":
        show_phase_1()
    elif page == "Phase 2":
        show_phase_2()
    elif page == "Phase 3":
        show_phase_3()
    elif page == "Phase 4":
        show_phase_4()
    elif page == "Documentation":
        show_documentation()
    elif page == "Conclusion":
        show_conclusion()


if __name__ == "__main__":
    main()

import streamlit as st


def show_introduction():
    st.title("MLOps Accidents Pipeline Project")

    st.image("images/pipeline.png", use_container_width=True)

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

    st.markdown("---")

    st.subheader("GitHub Repository")
    st.write(
        """
            Link to a repository on Github with a machine learning model:
            https://github.com/DataScientest-Studio/Template_MLOps_accidents
        """
    )

    st.markdown("---")

    st.subheader("Technology Stack")
    st.write(
        "The project follows a **phased approach**, progressively enhancing the pipeline:\n\n"

        "1. **Foundations:** GitHub setup → Model training → FastAPI → Testing\n"
        "2. **Tracking & Versioning:** MLflow | DVC | Docker\n"
        "3. **Orchestration:** Kubernetes | Jenkins\n"
        "4. **Monitoring:** Prometheus/Grafana | Evidently"
    )

    st.markdown("---")

    st.subheader("Project Goals")
    st.write(
        """
            ✅ Implement a **scalable API** for model inference (FastAPI)  
            ✅ Ensure **experiment tracking & reproducibility** (MLflow, DVC)  
            ✅ Automate **CI/CD pipelines** (Jenkins)  
            ✅ Enable **real-time monitoring** (Prometheus/Grafana, Evidently)  
            ✅ Containerize and **orchestrate** services (Docker, Kubernetes)  
        """
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

    st.subheader("MLlow: Experiment tracking")
    st.write(
        """
        MLflow is an open-source platform for managing the machine learning lifecycle.
        MLflow solves the chaos of model versioning and lets teams collaborate on ML development.
        """
    )

    st.badge(
        "**What was done:** Set up experiment tracking, logging of parameters/metrics, and a web UI.",
        color="green"
    )
    st.badge(
        "**Purpose:** To compare model versions and reproduce the best results.",
        color="green"
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

    st.badge(
        "**What was done:** Version control for datasets and models.",
        color="green"
    )
    st.badge(
        "**Purpose:** Ensures reproducibility and team collaboration.",
        color="green"
    )

    st.image("images/dvc_pipeline_1.jpg", caption="It's work!", use_container_width=True)
    st.image("images/dvc_pipeline_2.jpg", caption="DVC Pipeline Dependency Graph", use_container_width=True)
    st.write(
        """
        ### **Dependency Graph Explanation**  
        **`process_data`** → **`train`**  
        1. **`process_data`**:  
           - Preprocessing stage (raw data → data/raw).  
           - Output: Processed data (e.g., `data/preprocessed`).  
        
        2. **`train`**:  
           - Model training stage (uses processed data).  
           - Output: Trained model (e.g., `src/models/trained_model.joblib`).  
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

    st.badge(
        "**What was done:** Containerized the entire setup (FastAPI + MLflow).",
        color="green"
    )
    st.badge(
        "**Purpose:** Simplifies deployment and scaling.",
        color="green"
    )

    st.image("images/docker_workflow.png", use_container_width=True)

    st.subheader("Current Progress")
    st.write("A Docker container has been built during the development phase of our project.")
    st.image("images/docker_create.jpg", use_container_width=True)


def show_phase_3():
    st.title("Production Orchestration")
    st.image("images/conductor.png", use_container_width=True)

    st.write("text text text")

    st.subheader("Kubernetes: Scalable deployment")
    st.write("text text text")

    st.subheader("Jenkins: CI/CD pipelines")
    st.write("text text text")


def show_phase_4():
    st.title("Monitoring")
    st.image("images/dashboard.png", use_container_width=True)

    st.write("text text text")

    st.subheader("Grafana: Real-time dashboards")
    st.write("text text text")

    st.subheader("Evidently: Data drift detection")
    st.write("text text text")


def show_demo():
    st.title("Pipeline Demo")

    st.image("images/rocket.png", use_container_width=True)

    st.subheader("Pipeline demonstration")
    st.write("text text text")


def main():
    st.set_page_config(page_title="MLOps Accidents Project", page_icon="🚙", layout="wide")

    page = st.sidebar.radio(
        "Main menu", [
            "Introduction",
            "Phase 1 (Data)",
            "Phase 2 (Tracking)",
            "Phase 3 (Orchestration)",
            "Phase 4 (Monitoring)",
            "Demo"
        ]
    )

    if page == "Introduction":
        show_introduction()
    elif page == "Phase 1 (Data)":
        show_phase_1()
    elif page == "Phase 2 (Tracking)":
        show_phase_2()
    elif page == "Phase 3 (Orchestration)":
        show_phase_3()
    elif page == "Phase 4 (Monitoring)":
        show_phase_4()
    elif page == "Demo":
        show_demo()


if __name__ == "__main__":
    main()

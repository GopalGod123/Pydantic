# Patient Management System API

This project is a FastAPI-based Patient Management System that demonstrates advanced usage of [Pydantic](https://docs.pydantic.dev/) for data validation, computed fields, nested models, and serialization. It provides a RESTful API for managing patient records, including CRUD operations and sorting/filtering capabilities.

## Features

- **Patient CRUD API**: Create, read, update, and delete patient records.
- **Computed Fields**: Automatic calculation of BMI and BMI category.
- **Field & Model Validators**: Custom validation logic for fields and models.
- **Nested Models**: Organization of related data (e.g., address).
- **Serialization**: Flexible serialization of models to JSON.
- **Data Storage**: Patient data is stored in a JSON file (`patients.json`).

## Project Structure

- [`main.py`](main.py): FastAPI application with all API endpoints.
- [`patients.json`](patients.json): Stores patient records.
- [`1_pydantic_why.py`](1_pydantic_why.py): Demonstrates Pydantic field and model validation.
- [`2_field_validator.py`](2_field_validator.py): Example of field validators.
- [`3_model_validator.py`](3_model_validator.py): Example of model validators.
- [`4_computed_fields.py`](4_computed_fields.py): Example of computed fields.
- [`5_nested_models.py`](5_nested_models.py): Example of nested models.
- [`6_serialization.py`](6_serialization.py): Example of model serialization.
- `.gitignore`: Ignores virtual environment and cache files.

## API Endpoints

- `GET /`: Welcome message.
- `GET /about`: API description.
- `GET /view`: View all patient records.
- `GET /patient/{patient_id}`: View a specific patient.
- `GET /sort`: Sort patients by height, weight, or BMI.
- `POST /create`: Create a new patient.
- `PUT /update/{patient_id}`: Update an existing patient.
- `DELETE /delete/{patient_id}`: Delete a patient.

## Getting Started

1. **Install dependencies**:
    ```sh
    pip install fastapi pydantic uvicorn
    ```

2. **Run the API server**:
    ```sh
    uvicorn main:app --reload
    ```

3. **Access the API docs**:
    - Open [http://localhost:8000/docs](http://localhost:8000/docs) in your browser.

## Example Patient Data

See [`patients.json`](patients.json) for sample patient records.

## Notes

- The API uses Pydantic's advanced features for validation and computed fields.
- For demonstration, patient data is stored in a local JSON file.
- See the individual Python files for more examples of Pydantic usage.

## License

This project is for educational purposes.
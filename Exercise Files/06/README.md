Test the model locally:

    gcloud ml-engine local predict --model-dir=exported_model/ --json-instances=sample_input_prescaled.json

Create the bucket in a European server: 

    gsutil mb -l europe-west1 gs://tfclass-linkedin-vitojph

Upload the model:

    gsutil cp -R exported_model/* gs://tfclass-linkedin-vitojph/earnings-v1

Tell GCloud to create the model

    gcloud ml-engine models create earnings --regions europe-west1

Create the first version of the model

    gcloud ml-engine versions create v1 --model=earnings --origin=gs://tfclass-linkedin-vitojph/earnings-v1

Test the model using a sample json file

    gcloud ml-engine predict --model=earnings --json-instances=sample_input_prescaled.json


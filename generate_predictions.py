import argparse
import json
import subprocess

def generate_predictions(dataset):
    predictions = {}
    for article in dataset:
        for paragraph in article['paragraphs']:
            context = paragraph['context']
            # create instance of model for paragraph of text here (context == text of paragraph)

            for qa in paragraph['qas']:
                question = qa['question']
                # feed question into model here
                answer = 'example answer'
                predictions[qa['id']] = answer
    return predictions


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Runs a model on all testing inputs and creates the corresponding output file')
    parser.add_argument('dataset_file', help='Dataset file')
    parser.add_argument('output_file', help='Name of file to create')
    # TODO: decide how to choose the model/model options (part of command line?)

    args = parser.parse_args()
    with open(args.dataset_file) as dataset_file:
        dataset_json = json.load(dataset_file)
        dataset = dataset_json['data']

        # generate predictions and save to a file
        predictions = generate_predictions(dataset)
        with open(args.output_file, 'w') as output_file:
            json.dump(predictions, output_file)
            output_file.close()

            # run the check script on the generated prediction file
            print subprocess.check_output(["python", "evaluate-v1.1.py", args.dataset_file, args.output_file])

# Annotation code and explanation 

## Steps taken for annotation
- Preparation of annotation file for each annotator (Intermediate file)
- Assignment of Intermediate Files to each annotator.
- Collation of Intermediate Files i.e files annotated by individual annotators into one file.
- The details of all these processes are described in the following sections below. 

## Intermediate Files
The annotation task was equally divided between all 4 project members. Each document was randomly assigned to 3 annotators. 
Each document contains the column `content`(post content) which for our use case can be considered as a document that needs to be assigned one label (from 1 to 6). 
For each project member a csv file was generated so that each annotator can start annotating their files. 

The code used for generating these csv files:
- **Storage Path:** [`src/corpus_collection_analysis.ipynb`](src/corpus_collection_analysis.ipynb)
- See the section `Creating four different data files for annotators`.

### Location of Intermediate Files for each annotator

| Annotator Name | Location |
|------|----------|
| Kartik  | [`data/Annotation_instances/linkedIn_data_Kartik.csv`](data/Annotation_instances/linkedIn_data_Kartik.csv) |
| Muhammad | [`data/Annotation_instances/linkedIn_data_Muhammad.csv`](data/Annotation_instances/linkedIn_data_Muhammad.csv) |
| Timothy | [`data/Annotation_instances/linkedIn_data_Timothy.csv`](data/Annotation_instances/linkedIn_data_Timothy.csv) |
| Zhengyi | [`data/Annotation_instances/linkedIn_data_Zhengyi.csv`](data/Annotation_instances/linkedIn_data_Zhengyi.csv) |

### Code for generating Annotation File
- **Storage Path:** [`src/data_annotation.ipynb`](src/data_annotation.ipynb)

### Combined File for Inter Annotator Agreement Analysis
- **File Path:**
[`data/Annotation_instances/linkedin_combined_annotation.csv`](data/Annotation_instances/linkedin_combined_annotation.csv)

## Final Annotation file
- **File Path:**
[`data/annotated_data.csv`](data/annotated_data.csv)
- A CSV file that contains `content`(this is the content of the post) and `label`. `content` can be thought of as a document. `label` is a categorical value ('Professional Growth', 'Events', 'Interactive Promotions', 'Educational Resources', 'Trends', 'Others') that is the final label assigned to each `content`. Apart from this the file also contains post statistics like views, hashtags, etc.

## Challenges & Discussion:
- To ensure that annotation doesn't take a long time. We used labels like 1, 2, 3, etc, instead of their actual names like 'Events', 'Professional growth'.
- The `content` length for some posts was really long. This made it difficult sometimes to annotate these. Some annotators decided to print them on the terminal to view them clearly, while others formatted them using tools like Excel.
- One other challenge was collating the final document to get all the labels. Initially, we had not assigned a unique identifier like index. Collating them based on post content was getting difficult, so we decided to add an  index to ease the process of identification.

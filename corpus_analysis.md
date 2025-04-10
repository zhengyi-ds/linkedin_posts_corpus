# Corpus Analysis

## Code Used
- **Storage Path:** [`src/corpus_collection_analysis.ipynb`](src/corpus_collection_analysis.ipynb)

## Overview
This analysis compares the statistical properties of the given corpus (Posts) to the Brown Corpus, a well-known balanced corpus of American English texts. The comparison provides insights into lexical diversity, word usage, and sentence structure.

## Statistical Comparison
| Statistic                 | Brown Corpus      | Posts            |
|---------------------------|------------------|------------------|
| Number of Words          | 992,910          | 76,184           |
| Number of Sentences      | 55,578           | 4,938            |
| Average Word Length      | 4.678            | 4.886            |
| Vocabulary Size          | 40,669           | 11,846           |
| Lexical Diversity        | 0.04096          | 0.15549          |
| Hapax Legomena          | 15,538           | 6,558            |
| Average Sentence Length | 17.87            | 15.43            |
| Type-to-Token Ratio      | 0.04096          | 0.15549          |

## Key Observations

### 1. **Lexical Diversity and Type-to-Token Ratio**
- The Posts corpus exhibits significantly higher lexical diversity (0.1555) compared to the Brown Corpus (0.0410).
- This suggests that the language in the Posts corpus is more varied, possibly due to the nature of online discussions where new words, slang, or domain-specific terminology are used frequently.

### 2. **Vocabulary Size and Hapax Legomena**
- The Posts corpus has a smaller vocabulary size (11,846 words) compared to the Brown Corpus (40,669 words), but a relatively high number of hapax legomena (6,558 words vs. 15,538 words).
- This indicates that while the total number of unique words is lower, a substantial proportion of words are used only once, which is typical of informal or user-generated content.

### 3. **Word and Sentence Length**
- The average word length is slightly higher in the Posts corpus (4.886 vs. 4.678), which might indicate the presence of more complex or technical vocabulary.
- The average sentence length is shorter in the Posts corpus (15.43 words per sentence vs. 17.87), reflecting a more conversational and less formal writing style, common in social media or online discussions.

## Conclusion
The Posts corpus demonstrates significant linguistic differences compared to the Brown Corpus, characterized by greater lexical diversity, shorter sentences, and a higher proportion of unique words. These findings align with expectations for user-generated online content, where informal language and evolving vocabulary are prominent.

Further research could involve comparing the Posts corpus to other modern corpora (e.g., Twitter, Reddit, or blog datasets) to better contextualize these findings.

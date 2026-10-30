# Requirement → Deliverable checklist

Status legend: ✅ implemented and verified in Docker · 👤 must be done by the team (needs your accounts or machines)

Notebook section numbers refer to `notebook/analysis.ipynb`. Figures are in `output/figures/`.

## 2. Project structure

| Requirement | Implementation / evidence | Status |
|---|---|---|
| `bd-a1/` with Dockerfile, requirements.txt, README.md, data/dataset.csv, notebook/analysis.ipynb, output/{cleaned_data.csv, model_metrics.txt, cluster_summary.txt, figures/}, screenshots/ | Repository tree (README §3) | ✅ |
| Files prepared on the host before building | Dataset + notebook are `COPY`'d from the host in the Dockerfile | ✅ |

## 3. Docker environment and reproducibility [5 marks]

| Req. | Marks | Implementation / evidence | Status |
|---|---|---|---|
| 3.1 Base `quay.io/jupyter/scipy-notebook:latest` | 2 | `Dockerfile` line `FROM quay.io/jupyter/scipy-notebook:latest` | ✅ |
| 3.1 Extra packages via requirements.txt | | `RUN pip install --no-cache-dir -r /tmp/requirements.txt` (installed `tabulate`, the others are already satisfied) | ✅ |
| 3.1 Create folder, copy notebook + dataset | | `RUN mkdir -p ${PROJECT_DIR}/...` and two `COPY` lines | ✅ |
| 3.1 WORKDIR = created folder | | `WORKDIR ${PROJECT_DIR}` (= `/home/jovyan/bd-a1`); `docker inspect` shows `WorkingDir` | ✅ |
| 3.2 Open JupyterLab, execute notebook in container | 1 | `CMD start-notebook.py ...`; the notebook was executed inside the container (cell 1 prints `Running inside Docker: True`) | ✅ (screenshots 👤) |
| 3.2 README: image vs container, `HOST_PORT:CONTAINER_PORT` | | README §6 | ✅ |
| 3.3 Bind mount, outputs persist after container removal | 1 | `-v "$(pwd)/output:/home/jovyan/bd-a1/output"`, explained in README §8. `docs/validation/docker_validation_log.txt` shows the files still on the host after `docker rm` | ✅ |
| 3.4 `docker images`, `ps`, `ps -a`, `logs`, `inspect` | 0.5 | README §11 (table + lifecycle diagram); real output in `docs/validation/docker_validation_log.txt` | ✅ (screenshots 👤) |
| 3.4 Screenshots of image + running container | | List in `screenshots/README.md` | 👤 |
| 3.5 Tag with Docker Hub username, push, document repo:tag | 0.5 | README §12, `ayhamayman/bd-a1:v1` | 👤 login + push |
| 3.5 Teammate pulls and runs | | README §13 | 👤 |
| Image layers explained | (discussion) | README §5 "Docker image layers" | ✅ |
| Container lifecycle explained | (discussion) | README §11 "Container lifecycle" | ✅ |

## 4. Data analysis and preprocessing [5 marks]

| Requirement | Notebook evidence | Status |
|---|---|---|
| Load; head, shape, columns, dtypes, info, describe | §2 (`head(10)`, shape/columns/dtypes, `info()`, `describe(include="all")`, length stats per class) | ✅ |
| What one row represents; text / label / numerical columns | §2 markdown table + `describe_column_roles()` | ✅ |
| Missing values per column | §3.1 (NaN + empty/blank strings per column) | ✅ |
| Duplicates | §3.3: 403 exact duplicates (309 ham / 94 spam), 0 conflicting labels | ✅ |
| Treatment + justification | §3 "Cleaning decisions" + `clean_dataset()` | ✅ |
| Shape before/after | (5574, 2) → (5171, 2) | ✅ |
| `loc` conditional selection | §4: long call-to-action spam; ham questions | ✅ |
| `iloc` positional selection | §4: `iloc[0:5, 0]`, `iloc[100:105, :]` | ✅ |
| `iloc` with `np.r_` | §4: `np.r_[0:3, 50:53, -2:0]` and `iloc[np.r_[10:13], np.r_[0, 1]]` | ✅ |
| ≥ 3 transformations | §5: type conversion, label encoding, feature creation (8 features), binning, min-max + z-score normalization, category consolidation (6 types) | ✅ |
| Simple random / stratified / cluster sampling | §6 | ✅ |
| Compare distributions + explain differences | §6 table, `06_sampling_comparison.png`, 300-repetition experiment, written explanation | ✅ |
| ≥ 4 numerical text features | `char_count`, `word_count`, `unique_word_count`, `avg_word_length`, plus `digit_count`, `uppercase_ratio`, `exclamation_count` | ✅ |
| Correlation matrix + heatmap | §7, `01_correlation_heatmap.png` | ✅ |
| Interpret strong/weak; correlation ≠ causation | §7 ranked pairs + markdown | ✅ |

## 5. Text analysis [4 marks]

| Requirement | Notebook evidence | Status |
|---|---|---|
| New `cleaned_text`, original unchanged | §8 (`assert df["message"].equals(original_messages)`) | ✅ |
| Lowercase, missing text, punctuation, extra spaces, URLs/numbers | §8 `clean_text()` + unit asserts (also handles HTML entities, e-mails, currency) | ✅ |
| Tokenize; total tokens, unique words, avg words/record | §8: 81,818 tokens; 7,775 unique; 15.82 words/record | ✅ |
| Top-20 table + bar chart | §9 table, `02_word_frequency.png` | ✅ |
| Before/after stop-word removal (17/20 were stop words) | §9 side-by-side table + two-panel chart | ✅ |
| Spam vs ham: avg length, avg word count, top-10 words | §10 table, top-10 table, `03_spam_vs_ham_comparison.png` | ✅ |
| ≥ 5 insights (observation, evidence, interpretation) | §11: 6 insights; evidence computed in the preceding cell | ✅ |

## 6. Machine learning [4 marks]

| Requirement | Notebook evidence | Status |
|---|---|---|
| Label as target | `label_num` (spam = 1) | ✅ |
| Train/test split with stratification | 80/20, `stratify=y` (spam 12.62% / 12.66%) | ✅ |
| TF-IDF | `TfidfVectorizer(ngram_range=(1,2), min_df=2, sublinear_tf=True)` | ✅ |
| Classifier | Multinomial Naive Bayes + Logistic Regression | ✅ |
| Accuracy, precision, recall, F1 | §12 table, classification reports, `output/model_metrics.txt` | ✅ |
| Confusion matrix | `04_confusion_matrices_model_comparison.png` + matrices in `model_metrics.txt` | ✅ |
| Interpretation + limitation | §12 markdown (4 limitations) + error analysis | ✅ |
| No leakage | TF-IDF inside `Pipeline`, fitted on training data only; CV refits per fold; duplicates removed before the split | ✅ |
| K-Means on meaningful representation | TF-IDF → TruncatedSVD(100) → L2 normalisation (LSA) | ✅ |
| k chosen by experiment (not forced 3) | k = 2..10, inertia + silhouette, `05_kmeans_k_selection.png` → k = 9 | ✅ |
| Cluster sizes + silhouette | §13, `cluster_summary.txt` | ✅ |
| Top terms + interpretation per cluster | §13 profile table, representative messages, interpretation table | ✅ |
| Compare with labels; IDs ≠ classes | crosstab, purity / ARI / homogeneity, `07_clusters_vs_labels.png`, explanation | ✅ |

## 7. Required outputs and deliverables [2 marks]

| Deliverable | Location | Status |
|---|---|---|
| cleaned_data.csv | `output/cleaned_data.csv` (5,171 rows, 17 columns) | ✅ |
| ≥ 4 figures (heatmap, word frequency, group comparison, confusion matrix) | `output/figures/01`–`04` (+ 4 extra figures) | ✅ |
| model_metrics.txt | `output/model_metrics.txt` | ✅ |
| cluster_summary.txt (sizes, quality, interpretation) | `output/cluster_summary.txt` | ✅ |
| README with setup/build/run/mount/Docker Hub/reproduction | `README.md` | ✅ |
| Screenshots | `screenshots/` (see list) | 👤 |
| One ZIP of the complete project | `bd-a1.zip` | ✅ (update it after adding your screenshots) |

## 10. Bonus [+1 mark in the assignment PDF]

| Bonus | Implementation | Status |
|---|---|---|
| GitHub (+0.5) | `.gitignore`, structured repository, README §15 with git commands | ✅ prepared; 👤 create the repo and push |
| Model extension (+0.5) | Two classifiers compared (NB vs LR), word bigrams, 5-fold stratified CV | ✅ |

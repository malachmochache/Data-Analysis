# Load necessary library
if (!require("readr")) install.packages("readr", dependencies = TRUE)
library(readr)

# Define the ZIP file and the target directory
zip_file <- "Employee Profile.zip"
unzip_dir <- "Employee_Profile_Unzipped"

# Try unzipping the ZIP file
tryCatch({
  unzip(zip_file, exdir = unzip_dir)
  cat("ZIP file extracted to:", unzip_dir, "\n")
}, error = function(e) {
  cat("Error during unzipping:", e$message, "\n")
  stop("Terminating script due to unzip failure.")
})

# Try listing extracted files
files <- tryCatch({
  list.files(unzip_dir, full.names = TRUE)
}, error = function(e) {
  cat("Error listing extracted files:", e$message, "\n")
  character(0)
})

# Display the list of extracted files
if (length(files) == 0) {
  cat("No files found in the extracted directory.\n")
} else {
  cat("Extracted Files:\n")
  print(files)
}

# Filter CSV files
csv_files <- files[grepl("\\.csv$", files, ignore.case = TRUE)]

# Read and display CSV file
if (length(csv_files) > 0) {
  df <- tryCatch({
    read_csv(csv_files[1])
  }, error = function(e) {
    cat("Error reading CSV file:", e$message, "\n")
    NULL
  })
  
  if (!is.null(df)) {
    cat("CSV file loaded successfully. Here's a preview:\n")
    print(df)
  } else {
    cat("Failed to load the CSV file.\n")
  }
  
} else {
  cat("No CSV file found in the ZIP archive.\n")
}

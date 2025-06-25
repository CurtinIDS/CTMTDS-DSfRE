set -e

cd "$(dirname "$0")"

output_folder="rendered_slides"
output_format="pdf"


slides=`ls ../[0-9]*/*.qmd`

mkdir -p $output_folder
echo "Found slides are $slides"
for f in $slides
do
echo "Processing $f"
# Quarto file to render HAS to be before args
quarto render $f --output-dir $output_folder --to $output_format 
done
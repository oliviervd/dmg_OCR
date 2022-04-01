import pytesseract as pt
import pandas as pd
from PIL import Image
from utils.utils import pdf_to_page

##create excel
columns = ["ID_VAI", "bron", "originele naam ontwerp", "alternatieve naam ontwerp",
           "datum van ontwerp", "beshrijving ontwerp (nl)", "beschrijving ontwerp (en)",
           "prijs", "opmerkingen", "vrije trefwoorden", "" ]

pdf_file = "assets/fiches design centre deel 1.pdf"

pdf_to_page(pdf_file)
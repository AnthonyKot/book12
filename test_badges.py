import re, glob
import unicodedata

def normalize(text):
    return re.sub(r'\s+', ' ', text).strip().lower()

def check_zero(filename, term):
    with open(filename, 'r', encoding='utf-8') as f:
        content = normalize(f.read())
    # Regex for stem search if there's a *
    if '*' in term:
        regex = r'\b' + term.replace('*', r'\w*').lower()
    else:
        regex = r'\b' + term.lower() + r'\b'
    matches = re.findall(regex, content)
    return len(matches)

# Chapter 2 Badges
print("Ch2 AU invasion:", check_zero("corpus-orig/au-2020-our-common-bond-testable.txt", "invasion"))
print("Ch2 AU Cook:", check_zero("corpus-orig/au-2020-our-common-bond-testable.txt", "Cook"))
print("Ch2 AU 1770:", check_zero("corpus-orig/au-2020-our-common-bond-testable.txt", "1770"))
print("Ch2 AU terra nullius:", check_zero("corpus-orig/au-2020-our-common-bond-testable.txt", "terra nullius"))

print("Ch2 ES 711:", check_zero("corpus-orig/es-2026-manualccse.txt", "711"))
print("Ch2 ES visigod*:", check_zero("corpus-orig/es-2026-manualccse.txt", "visigod*"))
print("Ch2 ES Hispania:", check_zero("corpus-orig/es-2026-manualccse.txt", "Hispania"))
print("Ch2 ES 1812:", check_zero("corpus-orig/es-2026-manualccse.txt", "1812"))

print("Ch2 DE Weimar:", check_zero("corpus-orig/de-2025-bamf-gesamtfragenkatalog.txt", "Weimar"))
print("Ch2 DE Kaiser:", check_zero("corpus-orig/de-2025-bamf-gesamtfragenkatalog.txt", "Kaiser"))
print("Ch2 DE 1871:", check_zero("corpus-orig/de-2025-bamf-gesamtfragenkatalog.txt", "1871"))
print("Ch2 DE 1848:", check_zero("corpus-orig/de-2025-bamf-gesamtfragenkatalog.txt", "1848"))
print("Ch2 DE Luther:", check_zero("corpus-orig/de-2025-bamf-gesamtfragenkatalog.txt", "Luther"))

# Chapter 4 Badges
print("Ch4 AT Opfer:", check_zero("corpus-orig/at-2022-meinoesterreich.txt", "Opfer"))
print("Ch4 AT Waldheim:", check_zero("corpus-orig/at-2022-meinoesterreich.txt", "Waldheim"))
print("Ch4 AT 1986:", check_zero("corpus-orig/at-2022-meinoesterreich.txt", "1986"))
print("Ch4 DK Frikorps:", check_zero("corpus-orig/dk-2025-indfoedsretsproeven.txt", "Frikorps"))
print("Ch4 DK Waffen-SS:", check_zero("corpus-orig/dk-2025-indfoedsretsproeven.txt", "Waffen-SS"))
print("Ch4 DK østfront:", check_zero("corpus-orig/dk-2025-indfoedsretsproeven.txt", "østfront"))
print("Ch4 DK Theresienstadt:", check_zero("corpus-orig/dk-2025-indfoedsretsproeven.txt", "Theresienstadt"))
print("Ch4 EE Holocaust:", check_zero("corpus-orig/ee-2010-abikskodakondsuse-taotlejale.txt", "Holocaust"))
print("Ch4 EE holokaust:", check_zero("corpus-orig/ee-2010-abikskodakondsuse-taotlejale.txt", "holokaust"))
print("Ch4 EE Klooga:", check_zero("corpus-orig/ee-2010-abikskodakondsuse-taotlejale.txt", "Klooga"))

print("Ch4 CA Holocaust:", check_zero("corpus-orig/ca-2012r2021-discovercanada.txt", "Holocaust"))

print("Ch4 UK Holocaust:", check_zero("corpus-orig/uk-2013-lifeintheuk-retypeset.txt", "Holocaust"))
print("Ch4 UK concentration:", check_zero("corpus-orig/uk-2013-lifeintheuk-retypeset.txt", "concentration"))
print("Ch4 UK Auschwitz:", check_zero("corpus-orig/uk-2013-lifeintheuk-retypeset.txt", "Auschwitz"))
print("Ch4 UK internment:", check_zero("corpus-orig/uk-2013-lifeintheuk-retypeset.txt", "internment"))

print("Ch4 US Hitler:", check_zero("corpus-orig/us-2008-uscis-100q.txt", "Hitler"))
print("Ch4 US Nazi:", check_zero("corpus-orig/us-2008-uscis-100q.txt", "Nazi"))
print("Ch4 US Pearl Harbor:", check_zero("corpus-orig/us-2008-uscis-100q.txt", "Pearl Harbor"))
print("Ch4 US Holocaust:", check_zero("corpus-orig/us-2008-uscis-100q.txt", "Holocaust"))
print("Ch4 US Hiroshima:", check_zero("corpus-orig/us-2008-uscis-100q.txt", "Hiroshima"))
print("Ch4 US intern*:", check_zero("corpus-orig/us-2008-uscis-100q.txt", "intern*"))

print("Ch4 AU Kokoda:", check_zero("corpus-orig/au-2020-our-common-bond-testable.txt", "Kokoda"))
print("Ch4 AU Darwin bombing:", check_zero("corpus-orig/au-2020-our-common-bond-testable.txt", "Darwin bombing"))
print("Ch4 AU Singapore:", check_zero("corpus-orig/au-2020-our-common-bond-testable.txt", "Singapore"))
print("Ch4 AU Japan:", check_zero("corpus-orig/au-2020-our-common-bond-testable.txt", "Japan"))
print("Ch4 AU 1939:", check_zero("corpus-orig/au-2020-our-common-bond-testable.txt", "1939"))
print("Ch4 AU 1945:", check_zero("corpus-orig/au-2020-our-common-bond-testable.txt", "1945"))

print("Ch4 ES Guerra Mundial:", check_zero("corpus-orig/es-2026-manualccse.txt", "Guerra Mundial"))
print("Ch4 ES Hitler:", check_zero("corpus-orig/es-2026-manualccse.txt", "Hitler"))
print("Ch4 ES nazi:", check_zero("corpus-orig/es-2026-manualccse.txt", "nazi"))
print("Ch4 ES Holocausto:", check_zero("corpus-orig/es-2026-manualccse.txt", "Holocausto"))
print("Ch4 ES Mauthausen:", check_zero("corpus-orig/es-2026-manualccse.txt", "Mauthausen"))

# Chapter 5 Badges
print("Ch5 AU Stolen Generations:", check_zero("corpus-orig/au-2020-our-common-bond-testable.txt", "Stolen Generations"))
print("Ch5 AU Sorry:", check_zero("corpus-orig/au-2020-our-common-bond-testable.txt", "Sorry"))
print("Ch5 AU Mabo:", check_zero("corpus-orig/au-2020-our-common-bond-testable.txt", "Mabo"))
print("Ch5 AU native title:", check_zero("corpus-orig/au-2020-our-common-bond-testable.txt", "native title"))
print("Ch5 AU terra nullius:", check_zero("corpus-orig/au-2020-our-common-bond-testable.txt", "terra nullius"))
print("Ch5 AU massacre:", check_zero("corpus-orig/au-2020-our-common-bond-testable.txt", "massacre"))
print("Ch5 AU frontier:", check_zero("corpus-orig/au-2020-our-common-bond-testable.txt", "frontier"))
print("Ch5 AU dispossess*:", check_zero("corpus-orig/au-2020-our-common-bond-testable.txt", "dispossess*"))

print("Ch5 US Trail of Tears:", check_zero("corpus-orig/us-2008-uscis-100q.txt", "Trail of Tears"))
print("Ch5 US reservation:", check_zero("corpus-orig/us-2008-uscis-100q.txt", "reservation"))
print("Ch5 US treaty:", check_zero("corpus-orig/us-2008-uscis-100q.txt", "treaty"))
print("Ch5 US Wounded Knee:", check_zero("corpus-orig/us-2008-uscis-100q.txt", "Wounded Knee"))

print("Ch5 UK indigenous:", check_zero("corpus-orig/uk-2013-lifeintheuk-retypeset.txt", "indigenous"))
print("Ch5 UK aboriginal:", check_zero("corpus-orig/uk-2013-lifeintheuk-retypeset.txt", "aboriginal"))
print("Ch5 UK Maori:", check_zero("corpus-orig/uk-2013-lifeintheuk-retypeset.txt", "Maori"))
print("Ch5 UK First Nations:", check_zero("corpus-orig/uk-2013-lifeintheuk-retypeset.txt", "First Nations"))

print("Ch5 ES indígena:", check_zero("corpus-orig/es-2026-manualccse.txt", "indígena"))
print("Ch5 ES pueblos originarios:", check_zero("corpus-orig/es-2026-manualccse.txt", "pueblos originarios"))
print("Ch5 ES Cortés:", check_zero("corpus-orig/es-2026-manualccse.txt", "Cortés"))
print("Ch5 ES Pizarro:", check_zero("corpus-orig/es-2026-manualccse.txt", "Pizarro"))
print("Ch5 ES mestiz*:", check_zero("corpus-orig/es-2026-manualccse.txt", "mestiz*"))
print("Ch5 ES Sáhara:", check_zero("corpus-orig/es-2026-manualccse.txt", "Sáhara"))

print("Ch5 DE Ureinwohner:", check_zero("corpus-orig/de-2025-bamf-gesamtfragenkatalog.txt", "Ureinwohner"))
print("Ch5 DE indigen*:", check_zero("corpus-orig/de-2025-bamf-gesamtfragenkatalog.txt", "indigen*"))
print("Ch5 DE Kolonie:", check_zero("corpus-orig/de-2025-bamf-gesamtfragenkatalog.txt", "Kolonie"))
print("Ch5 DE Herero:", check_zero("corpus-orig/de-2025-bamf-gesamtfragenkatalog.txt", "Herero"))
print("Ch5 DE Minderheit:", check_zero("corpus-orig/de-2025-bamf-gesamtfragenkatalog.txt", "Minderheit"))
print("Ch5 DE Sorben:", check_zero("corpus-orig/de-2025-bamf-gesamtfragenkatalog.txt", "Sorben"))
print("Ch5 DE Friesen:", check_zero("corpus-orig/de-2025-bamf-gesamtfragenkatalog.txt", "Friesen"))
print("Ch5 DE Sinti/Roma:", check_zero("corpus-orig/de-2025-bamf-gesamtfragenkatalog.txt", "Sinti/Roma"))
print("Ch5 DE Dänen:", check_zero("corpus-orig/de-2025-bamf-gesamtfragenkatalog.txt", "Dänen"))


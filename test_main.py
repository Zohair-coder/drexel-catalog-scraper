import pytest
from main import scrape

def test_scrape_cs_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofcomputingandinformatics/computingandsecuritytechnology/#sampleplansofstudytext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_cst_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofcomputingandinformatics/computingandsecuritytechnology/#sampleplansofstudytext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_accounting_bs_ba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofbusiness/accounting/#sampleplanofstudytext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_animation_and_visual_effects_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofmediaartsanddesign/animationandvisualeffects/#sampleplanofstudybstext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_architectural_engineering_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofengineering/architecturalengineering/#sampleplanofstudybstext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_architectural_studies_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofmediaartsanddesign/architecturalstudiesbs/#sampleplanofstudytext"
    data = scrape(url)
    assert len(data) > 0

@pytest.mark.skip(reason="This plan has a significantly different heading")
def test_scrape_architecture_ba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofmediaartsanddesign/architecture/#sampleplanofstudy24text"
    data = scrape(url)
    assert len(data) > 0

@pytest.mark.skip(reason="This plan has a significantly different structure")
def test_scrape_rotc():
    url = "https://catalog.drexel.edu/additionalacademicprograms/armyrotc/#planofstudy4yeartext"
    data = scrape(url)
    assert len(data) > 0

@pytest.mark.skip(reason="This plan has a significantly different structure")
def test_scrape_arts_history_ba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofmediaartsanddesign/arthistory/#sampleplanofstudybatext"
    data = scrape(url)
    assert len(data) > 0

@pytest.mark.skip(reason="This plan has a significantly different structure")
def test_scrape_arts_history_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofmediaartsanddesign/arthistorybs/#sampleplanofstudytext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_behavorial_econ_bs():
    url = "https://catalog.drexel.edu/undergraduate/schoolofeconomics/behavioraleconomicsbusinessandorganizations/#sampleplanofstudytext"
    data = scrape(url)  
    assert len(data) > 0

def test_scrape_human_development_and_conselling():
    url = "https://catalog.drexel.edu/undergraduate/collegeofnursingandhealthprofessions/humandevelopingandcounseling/index.html#sampleplanofstudytext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_biological_sciences_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofartsandsciences/biologicalsciences/#sampleplansofstudybstext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_biomedical_engineering_bs():
    url = "https://catalog.drexel.edu/undergraduate/schoolofbioengscienceandhealthsystems/biomedicalengineering/#sampleplanofstudytext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_general_business_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofbusiness/generalbusiness/#sampleplanofstudybatext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_business_undeclared():
    url = "https://catalog.drexel.edu/undergraduate/collegeofbusiness/businessundeclared/index.html#sampleplanofstudytext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_business_and_data_engineering():
    url = "https://catalog.drexel.edu/undergraduate/collegeofbusiness/businessandengineering/#sampleplanofstudytext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_business_analytics_bsba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofbusiness/businessanalytics/#sampleplanofstudytext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_general_business_bsba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofbusiness/generalbusiness/#sampleplanofstudybatext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_business_economics_bsba():
    url = "https://catalog.drexel.edu/undergraduate/schoolofeconomics/businesseconomics/index.html#sampleplanofstudytext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_chemical_engineering_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofengineering/chemicalengineering/#sampleplanofstudybstext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_chemistry_ba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofartsandsciences/chemistry/#sampleplansofstudybabstext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_chemistry_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofartsandsciences/chemistrybs/#sampleplanofstudytext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_biochem_concentration_chemistry_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofartsandsciences/chemistrybs/#biochemistryconcentrationsampleplanofstudytext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_civil_engineering_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofengineering/civilengineering/#sampleplanofstudybstext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_communication_ba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofengineering/civilengineering/#sampleplanofstudybstext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_computer_engineering_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofengineering/civilengineering/#sampleplanofstudybstext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_computer_science_ba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofcomputingandinformatics/computerscienceba/#sampleplanofstudytext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_computer_science_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofcomputingandinformatics/computerscience/#sampleplanofstudybstext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_computing_and_security_technology():
    url = "https://catalog.drexel.edu/undergraduate/collegeofcomputingandinformatics/computingandsecuritytechnology/#sampleplansofstudytext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_construction_management_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofengineering/constructionmanagement/#sampleplanofstudytext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_culinary_arts_and_science_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofnursingandhealthprofessions/culinaryartsandscience/index.html#sampleplanofstudytext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_custom_designed_bs():
    url = "https://catalog.drexel.edu/undergraduate/honorscollege/custom-designedmajor/#sampleplanofstudytext"
    data = scrape(url)
    assert len(data) > 0

@pytest.mark.skip(reason="This plan has a significantly different structure")
def test_scrape_dance_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofmediaartsanddesign/dance/#sampleplanofstudybstext"
    data = scrape(url)
    assert len(data) > 0

@pytest.mark.skip(reason="This plan has a significantly different structure")
def test_scrape_dance_parttime_professional_option_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofmediaartsanddesign/dance_parttimeprofessional/index.html#sampleplanofstudytext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_data_science_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofcomputingandinformatics/datascience/#sampleplanofstudytext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_design_and_merchandising_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofmediaartsanddesign/designandmerchandising/#sampleplansofstudybstext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_digital_media_and_virtual_production_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofmediaartsanddesign/digitalmediaandvirtualproduction/#sampleplanofstudytext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_economic_analysis():
    url = "https://catalog.drexel.edu/undergraduate/schoolofeconomics/economics/#newitemtext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_economics_bs():
    url = "https://catalog.drexel.edu/undergraduate/schoolofeconomics/economicsbs/#sampleplanofstudytext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_economics_and_buisness_bs():
    url = "https://catalog.drexel.edu/undergraduate/schoolofeconomics/economicsandbusiness/#sampleplanofstudytext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_economics_and_data_science_bs():
    url = "https://catalog.drexel.edu/undergraduate/schoolofeconomics/economicsanddatascience/#sampleplanofstudytext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_economics_and_math_bs():
    url = "https://catalog.drexel.edu/undergraduate/schoolofeconomics/economicsandmathematics/#sampleplanofstudytext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_economics_and_public_health_bs():
    url = "https://catalog.drexel.edu/undergraduate/schoolofeconomics/economicsandmathematics/#sampleplanofstudytext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_elementery_education_noncertification_bs():
    url = "https://catalog.drexel.edu/undergraduate/schoolofeducation/education-noncertification/index.html"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_engineering_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofengineering/engineering/#sampleplanofstudybstext"
    data = scrape(url)
    assert len(data) > 0

@pytest.mark.skip(reason="This plan has a significantly different structure")
def test_scrape_engineering_undeclared():
    url = "https://catalog.drexel.edu/undergraduate/collegeofengineering/engineeringundeclared/index.html#sampleplanofstudytext"
    data = scrape(url)
    assert len(data) > 0

def test_scrape_english_ba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofartsandsciences/english-literaryconcentration/index.html#sampleplanofstudytext"
    data = scrape(url)
    assert len(data) > 0

def test_entertainmaint_and_arts_management_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofartsandsciences/english-literaryconcentration/index.html#sampleplanofstudytext"
    data = scrape(url)
    assert len(data) > 0

def test_entrepreneurship_and_innovation_ba():
    url = "https://catalog.drexel.edu/undergraduate/schoolofentrepreneurship/entrepreneurshipandinnovation/index.html#sampleplanofstudytext"
    data = scrape(url)
    assert len(data) > 0

@pytest.mark.skip(reason="This plan has a significantly different structure")
def test_entp_and_innovation_three_year_option():
    url = "https://catalog.drexel.edu/undergraduate/schoolofentrepreneurship/entrepreneurshipandinnovation-3year/index.html#sampleplanofstudytext"
    data = scrape(url)
    assert len(data) > 0

def test_environmental_engineering_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofengineering/environmentalengineering/#sampleplanofstudybstext"
    data = scrape(url)
    assert len(data) > 0

def test_environmental_science_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofartsandsciences/environmentalscience/#sampleplansofstudybstext"
    data = scrape(url)
    assert len(data) > 0

def test_environmental_studies_and_sustainability_ba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofartsandsciences/environmentalstudiesandsustainability/#sampleplanofstudytext"
    data = scrape(url)
    assert len(data) > 0

def test_esport_business_bsba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofbusiness/esportbusiness/index.html#sampleplanofstudytext"
    data = scrape(url)
    assert len(data) > 0

@pytest.mark.skip(reason="This plan has a significantly different structure")
def test_exercise_science_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofnursingandhealthprofessions/exercisescience/#sampleplanofstudytext"
    data = scrape(url)
    assert len(data) > 0

def test_fashion_design_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofmediaartsanddesign/fashiondesign/#sampleplansofstudybstext"
    data = scrape(url)
    assert len(data) > 0

def test_film_and_television_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofmediaartsanddesign/filmandtvproduction/index.html#sampleplanofstudytext"
    data = scrape(url)
    assert len(data) > 0

def test_finance_bsba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofbusiness/finance/#sampleplanofstudytext"
    data = scrape(url)
    assert len(data) > 0

def test_first_year_exploratory_studies():
    url = "https://catalog.drexel.edu/additionalacademicprograms/firstyearexploratorystudies/#sampleplanofstudytext"
    data = scrape(url)
    assert len(data) > 0

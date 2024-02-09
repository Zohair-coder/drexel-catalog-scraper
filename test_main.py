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
from plan_of_study_scraper import scrape_page

def test_scrape_accounting_bs_ba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofbusiness/accounting/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_animation_and_visual_effects_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofmediaartsanddesign/animationandvisualeffects/#sampleplanofstudybstext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_architectural_engineering_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofengineering/architecturalengineering/#sampleplanofstudybstext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_architectural_studies_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofmediaartsanddesign/architecturalstudiesbs/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_architecture_ba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofmediaartsanddesign/architecture/#sampleplanofstudy24text"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_rotc():
    url = "https://catalog.drexel.edu/additionalacademicprograms/armyrotc/#planofstudy4yeartext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_arts_history_ba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofmediaartsanddesign/arthistory/#sampleplanofstudybatext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_arts_history_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofmediaartsanddesign/arthistorybs/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_behavorial_econ_bs():
    url = "https://catalog.drexel.edu/undergraduate/schoolofeconomics/behavioraleconomicsbusinessandorganizations/#sampleplanofstudytext"
    data = scrape_page(url)  
    assert len(data) > 0

def test_scrape_human_development_and_conselling():
    url = "https://catalog.drexel.edu/undergraduate/collegeofnursingandhealthprofessions/humandevelopingandcounseling/index.html#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_biological_sciences_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofartsandsciences/biologicalsciences/#sampleplansofstudybstext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_biomedical_engineering_bs():
    url = "https://catalog.drexel.edu/undergraduate/schoolofbioengscienceandhealthsystems/biomedicalengineering/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_general_business_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofbusiness/generalbusiness/#sampleplanofstudybatext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_business_undeclared():
    url = "https://catalog.drexel.edu/undergraduate/collegeofbusiness/businessundeclared/index.html#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_business_and_data_engineering():
    url = "https://catalog.drexel.edu/undergraduate/collegeofbusiness/businessandengineering/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_business_analytics_bsba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofbusiness/businessanalytics/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_general_business_bsba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofbusiness/generalbusiness/#sampleplanofstudybatext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_business_economics_bsba():
    url = "https://catalog.drexel.edu/undergraduate/schoolofeconomics/businesseconomics/index.html#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_chemical_engineering_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofengineering/chemicalengineering/#sampleplanofstudybstext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_chemistry_ba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofartsandsciences/chemistry/#sampleplansofstudybabstext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_chemistry_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofartsandsciences/chemistrybs/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_biochem_concentration_chemistry_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofartsandsciences/chemistrybs/#biochemistryconcentrationsampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_civil_engineering_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofengineering/civilengineering/#sampleplanofstudybstext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_communication_ba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofengineering/civilengineering/#sampleplanofstudybstext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_computer_engineering_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofengineering/civilengineering/#sampleplanofstudybstext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_computer_science_ba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofcomputingandinformatics/computerscienceba/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_computer_science_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofcomputingandinformatics/computerscience/#sampleplanofstudybstext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_computing_and_security_technology():
    url = "https://catalog.drexel.edu/undergraduate/collegeofcomputingandinformatics/computingandsecuritytechnology/#sampleplansofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_construction_management_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofengineering/constructionmanagement/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_culinary_arts_and_science_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofnursingandhealthprofessions/culinaryartsandscience/index.html#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_custom_designed_bs():
    url = "https://catalog.drexel.edu/undergraduate/honorscollege/custom-designedmajor/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_dance_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofmediaartsanddesign/dance/#sampleplanofstudybstext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_dance_parttime_professional_option_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofmediaartsanddesign/dance_parttimeprofessional/index.html#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_data_science_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofcomputingandinformatics/datascience/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_design_and_merchandising_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofmediaartsanddesign/designandmerchandising/#sampleplansofstudybstext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_digital_media_and_virtual_production_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofmediaartsanddesign/digitalmediaandvirtualproduction/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_economic_analysis():
    url = "https://catalog.drexel.edu/undergraduate/schoolofeconomics/economics/#newitemtext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_economics_bs():
    url = "https://catalog.drexel.edu/undergraduate/schoolofeconomics/economicsbs/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_economics_and_buisness_bs():
    url = "https://catalog.drexel.edu/undergraduate/schoolofeconomics/economicsandbusiness/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_economics_and_data_science_bs():
    url = "https://catalog.drexel.edu/undergraduate/schoolofeconomics/economicsanddatascience/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_economics_and_math_bs():
    url = "https://catalog.drexel.edu/undergraduate/schoolofeconomics/economicsandmathematics/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_economics_and_public_health_bs():
    url = "https://catalog.drexel.edu/undergraduate/schoolofeconomics/economicsandmathematics/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_elementery_education_noncertification_bs():
    url = "https://catalog.drexel.edu/undergraduate/schoolofeducation/education-noncertification/index.html"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_engineering_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofengineering/engineering/#sampleplanofstudybstext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_engineering_undeclared():
    url = "https://catalog.drexel.edu/undergraduate/collegeofengineering/engineeringundeclared/index.html#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_scrape_english_ba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofartsandsciences/english-literaryconcentration/index.html#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_entertainmaint_and_arts_management_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofartsandsciences/english-literaryconcentration/index.html#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_entrepreneurship_and_innovation_ba():
    url = "https://catalog.drexel.edu/undergraduate/schoolofentrepreneurship/entrepreneurshipandinnovation/index.html#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_entp_and_innovation_three_year_option():
    url = "https://catalog.drexel.edu/undergraduate/schoolofentrepreneurship/entrepreneurshipandinnovation-3year/index.html#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_environmental_engineering_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofengineering/environmentalengineering/#sampleplanofstudybstext"
    data = scrape_page(url)
    assert len(data) > 0

def test_environmental_science_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofartsandsciences/environmentalscience/#sampleplansofstudybstext"
    data = scrape_page(url)
    assert len(data) > 0

def test_environmental_studies_and_sustainability_ba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofartsandsciences/environmentalstudiesandsustainability/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_esport_business_bsba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofbusiness/esportbusiness/index.html#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_exercise_science_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofnursingandhealthprofessions/exercisescience/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_fashion_design_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofmediaartsanddesign/fashiondesign/#sampleplansofstudybstext"
    data = scrape_page(url)
    assert len(data) > 0

def test_film_and_television_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofmediaartsanddesign/filmandtvproduction/index.html#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_finance_bsba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofbusiness/finance/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_first_year_exploratory_studies():
    url = "https://catalog.drexel.edu/additionalacademicprograms/firstyearexploratorystudies/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_game_design_and_production_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofmediaartsanddesign/gamedesignandproduction/index.html#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_general_business_bsba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofbusiness/generalbusiness/#sampleplanofstudybatext"
    data = scrape_page(url)
    assert len(data) > 0

def test_general_humanities_and_social_sciences_undeclared():
    url = "https://catalog.drexel.edu/undergraduate/collegeofartsandsciences/generalhumanitiesandsocialsciences_undeclared/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_general_studies_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofprofessionalstudies/generalstudies/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_geoscience_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofartsandsciences/geoscience/#sampleplansofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_global_public_health_ba():
    url = "https://catalog.drexel.edu/undergraduate/schoolofpublichealth/globalpublichealth/index.html#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_global_studies_ba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofartsandsciences/globalstudies/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_graphic_design_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofmediaartsanddesign/graphicdesign/#sampleplanofstudybstext"
    data = scrape_page(url)
    assert len(data) > 0

def test_health_data_analytics_bs():
    url = "https://catalog.drexel.edu/undergraduate/schoolofpublichealth/healthdataanalytics/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_health_sciences_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofnursingandhealthprofessions/healthsciences/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_health_services_administration_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofnursingandhealthprofessions/healthservicesadministration/#sampleplanofstudybstext"
    data = scrape_page(url)
    assert len(data) > 0

def test_history_ba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofartsandsciences/history/#sampleplanofstudybatext"
    data = scrape_page(url)
    assert len(data) > 0

def test_hospitality_management_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofnursingandhealthprofessions/hospitalitymanagement/index.html#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_human_development_and_counseling():
    url = "https://catalog.drexel.edu/undergraduate/collegeofnursingandhealthprofessions/humandevelopingandcounseling/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_information_systems_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofcomputingandinformatics/informationsystems/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_international_business_bsba():
    url = "https://catalog.drexel.edu/undergraduate/schoolofeconomics/internationalbusiness/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_international_business_comajor_bsba():
    url = "https://catalog.drexel.edu/undergraduate/schoolofeconomics/internationalbusinesscomajor/index.html#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_interior_design_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofmediaartsanddesign/interiordesign/#sampleplansofstudybstext"
    data = scrape_page(url)
    assert len(data) > 0

def test_law_ba():
    url = "https://catalog.drexel.edu/undergraduate/schooloflaw/law/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_learning_sciences_experience_design_and_technology_bs():
    url = "https://catalog.drexel.edu/undergraduate/schoolofeducation/learningsciencesexperiencedesigntechnology/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_legal_studies_bsba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofbusiness/legalstudies/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_management_information_systems_bsba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofbusiness/managementinformationsystems/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_marketing_bsba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofbusiness/marketing/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_materials_science_and_engineering_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofengineering/materialsscienceandengineering/#sampleplanofstudybstext"
    data = scrape_page(url)
    assert len(data) > 0

def test_mathematical_statistics_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofartsandsciences/mathstatistics/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_mathematics_ba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofartsandsciences/mathematics/#sampleplansofstudybabstext"
    data = scrape_page(url)
    assert len(data) > 0

def test_mathematics_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofartsandsciences/mathematicsbs/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_mechanical_engineering_and_mechanics_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofengineering/mechanicalengineering/#sampleplanofstudybstext"
    data = scrape_page(url)
    assert len(data) > 0

def test_music_industry_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofmediaartsanddesign/musicindustry/#planofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_naval_rotc():
    url = "https://catalog.drexel.edu/additionalacademicprograms/navyrotc/index.html#planofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_neuroscience_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofartsandsciences/neuroscience/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_nursing_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofnursingandhealthprofessions/nursing/#sampleplansofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_nutrition_and_foods_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofnursingandhealthprofessions/nutritionandfoods/#sampleplanofstudybstext"
    data = scrape_page(url)
    assert len(data) > 0

def test_operations_and_supply_chain_management_bsba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofbusiness/operationandsupplychainmanagement/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_organizational_management_bsba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofbusiness/organizationalmanagement/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_philosophy_ba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofartsandsciences/philosophy/#sampleplanofstudybatext"
    data = scrape_page(url)
    assert len(data) > 0

def test_philosophy_politics_and_economics_ba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofartsandsciences/philosophypoliticseconomics/index.html#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_photography_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofmediaartsanddesign/photography/#sampleplansofstudybstext"
    data = scrape_page(url)
    assert len(data) > 0

def test_physics_ba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofartsandsciences/physics/#sampleplanofstudybstext"
    data = scrape_page(url)
    assert len(data) > 0

def test_political_science_ba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofartsandsciences/politicalscience/#sampleplanofstudybatext"
    data = scrape_page(url)
    assert len(data) > 0

def test_product_design_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofmediaartsanddesign/productdesign/#sampleplanofstudybstext"
    data = scrape_page(url)
    assert len(data) > 0

def test_psychology_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofartsandsciences/psychology/#sampleplanofstudybstext"
    data = scrape_page(url)
    assert len(data) > 0

def test_public_health_bs():
    url = "https://catalog.drexel.edu/undergraduate/schoolofpublichealth/publichealth/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_real_estate_management_and_development_bsba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofbusiness/realestatemanagementanddevelopment/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_science_undeclared():
    url = "https://catalog.drexel.edu/undergraduate/collegeofartsandsciences/scienceundeclared/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_screenwriting_and_playwriting_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofmediaartsanddesign/screenwritingandplaywriting/#sampleplanofstudybstext"
    data = scrape_page(url)
    assert len(data) > 0

def test_sociology_ba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofartsandsciences/sociology/#sampleplanofstudybatext"
    data = scrape_page(url)
    assert len(data) > 0

def test_software_engineering_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofcomputingandinformatics/softwareengineering/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_special_education_bs():
    url = "https://catalog.drexel.edu/undergraduate/schoolofeducation/specialeducationpk-12/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_sport_business_bsba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofbusiness/sportbusiness/index.html#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_sustainability_and_innovation_bs():
    url = "https://catalog.drexel.edu/undergraduate/schoolofentrepreneurship/sustainabilityandinnovationbs/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_technology_innovation_management_bsba():
    url = "https://catalog.drexel.edu/undergraduate/collegeofbusiness/technologyinnovationmanagement/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_user_experience_and_interaction_design_bs():
    url = "https://catalog.drexel.edu/undergraduate/collegeofmediaartsanddesign/userexperienceandinteractiondesign/#sampleplanofstudytext"
    data = scrape_page(url)
    assert len(data) > 0

def test_fake():
    url = "https://catalog.drexel.edu/additionalacademicprograms/airforcerotc/#sampleplanofstudy"
    data = scrape_page(url)
    assert len(data) == 0
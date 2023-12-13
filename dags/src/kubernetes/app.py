# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     user_input = request.form.get('text_input')
#     print(user_input)
#     return render_template('index.html', submitted_text=user_input)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080)

from flask import Flask, render_template, request
from typing import Dict, List, Union
from google.cloud import aiplatform
from google.protobuf import json_format
from google.protobuf.struct_pb2 import Value


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', submitted_text=None)

@app.route('/submit', methods=['POST'])
def submit_form():
    user_input = request.form.get('user_input')
    print(user_input)
    output = predict_custom_trained_model(
    project="187766244340",
    endpoint_id="7434695316881801216",
    location="us-east1",
    instances= {
        "text_input":user_input
        })
    print(user_input, output)
    output_name = list()
    names = ['O',
    'B-AccrualForEnvironmentalLossContingencies',
    'B-AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife',
    'I-AcquiredFiniteLivedIntangibleAssetsWeightedAverageUsefulLife',
    'B-AllocatedShareBasedCompensationExpense',
    'B-AmortizationOfFinancingCosts',
    'B-AmortizationOfIntangibleAssets',
    'I-AmortizationOfIntangibleAssets',
    'B-AntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareAmount',
    'I-AntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareAmount',
    'B-AreaOfRealEstateProperty',
    'I-AreaOfRealEstateProperty',
    'B-AssetImpairmentCharges',
    'B-BusinessAcquisitionEquityInterestsIssuedOrIssuableNumberOfSharesIssued',
    'B-BusinessAcquisitionPercentageOfVotingInterestsAcquired',
    'I-BusinessAcquisitionPercentageOfVotingInterestsAcquired',
    'B-BusinessCombinationAcquisitionRelatedCosts',
    'B-BusinessCombinationConsiderationTransferred1',
    'B-BusinessCombinationContingentConsiderationLiability',
    'B-BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedIntangibleAssetsOtherThanGoodwill',
    'B-BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedIntangibles',
    'B-CapitalizedContractCostAmortization',
    'B-CashAndCashEquivalentsFairValueDisclosure',
    'B-ClassOfWarrantOrRightExercisePriceOfWarrantsOrRights1',
    'B-CommonStockCapitalSharesReservedForFutureIssuance',
    'B-CommonStockDividendsPerShareDeclared',
    'B-CommonStockParOrStatedValuePerShare',
    'B-CommonStockSharesAuthorized',
    'I-CommonStockSharesAuthorized',
    'B-CommonStockSharesOutstanding',
    'B-ConcentrationRiskPercentage1',
    'B-ContractWithCustomerLiability',
    'B-ContractWithCustomerLiabilityRevenueRecognized',
    'B-CumulativeEffectOfNewAccountingPrincipleInPeriodOfAdoption',
    'B-DebtInstrumentBasisSpreadOnVariableRate1',
    'B-DebtInstrumentCarryingAmount',
    'B-DebtInstrumentConvertibleConversionPrice1',
    'B-DebtInstrumentFaceAmount',
    'I-DebtInstrumentFaceAmount',
    'B-DebtInstrumentFairValue',
    'B-DebtInstrumentInterestRateEffectivePercentage',
    'B-DebtInstrumentInterestRateStatedPercentage',
    'B-DebtInstrumentMaturityDate',
    'I-DebtInstrumentMaturityDate',
    'B-DebtInstrumentRedemptionPricePercentage',
    'B-DebtInstrumentTerm',
    'I-DebtInstrumentTerm',
    'B-DebtInstrumentUnamortizedDiscount',
    'B-DebtWeightedAverageInterestRate',
    'B-DeferredFinanceCostsGross',
    'B-DeferredFinanceCostsNet',
    'B-DefinedBenefitPlanContributionsByEmployer',
    'B-DefinedContributionPlanCostRecognized',
    'B-Depreciation',
    'B-DerivativeFixedInterestRate',
    'B-DerivativeNotionalAmount',
    'B-DisposalGroupIncludingDiscontinuedOperationConsideration',
    'B-EffectiveIncomeTaxRateContinuingOperations',
    'B-EffectiveIncomeTaxRateReconciliationAtFederalStatutoryIncomeTaxRate',
    'B-EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognized',
    'B-EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognizedPeriodForRecognition1',
    'I-EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognizedPeriodForRecognition1',
    'B-EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognizedShareBasedAwardsOtherThanOptions',
    'B-EmployeeServiceShareBasedCompensationTaxBenefitFromCompensationExpense',
    'B-EquityMethodInvestmentOwnershipPercentage',
    'I-EquityMethodInvestmentOwnershipPercentage',
    'B-EquityMethodInvestments',
    'B-FiniteLivedIntangibleAssetUsefulLife',
    'I-FiniteLivedIntangibleAssetUsefulLife',
    'B-GainsLossesOnExtinguishmentOfDebt',
    'B-Goodwill',
    'B-GoodwillImpairmentLoss',
    'B-GuaranteeObligationsMaximumExposure',
    'B-IncomeLossFromEquityMethodInvestments',
    'B-IncomeTaxExpenseBenefit',
    'B-InterestExpense',
    'B-InterestExpenseDebt',
    'B-LeaseAndRentalExpense',
    'B-LesseeOperatingLeaseRenewalTerm',
    'I-LesseeOperatingLeaseRenewalTerm',
    'B-LesseeOperatingLeaseTermOfContract',
    'I-LesseeOperatingLeaseTermOfContract',
    'B-LettersOfCreditOutstandingAmount',
    'B-LineOfCredit',
    'B-LineOfCreditFacilityCommitmentFeePercentage',
    'B-LineOfCreditFacilityCurrentBorrowingCapacity',
    'B-LineOfCreditFacilityInterestRateAtPeriodEnd',
    'B-LineOfCreditFacilityMaximumBorrowingCapacity',
    'B-LineOfCreditFacilityRemainingBorrowingCapacity',
    'B-LineOfCreditFacilityUnusedCapacityCommitmentFeePercentage',
    'B-LongTermDebt',
    'B-LongTermDebtFairValue',
    'B-LossContingencyAccrualAtCarryingValue',
    'B-LossContingencyDamagesSoughtValue',
    'B-LossContingencyEstimateOfPossibleLoss',
    'B-LossContingencyPendingClaimsNumber',
    'I-LossContingencyPendingClaimsNumber',
    'B-MinorityInterestOwnershipPercentageByNoncontrollingOwners',
    'B-MinorityInterestOwnershipPercentageByParent',
    'B-NumberOfOperatingSegments',
    'B-NumberOfRealEstateProperties',
    'I-NumberOfRealEstateProperties',
    'B-NumberOfReportableSegments',
    'B-OperatingLeaseCost',
    'B-OperatingLeaseExpense',
    'B-OperatingLeaseLiability',
    'B-OperatingLeasePayments',
    'B-OperatingLeaseRightOfUseAsset',
    'B-OperatingLeaseWeightedAverageDiscountRatePercent',
    'B-OperatingLeaseWeightedAverageRemainingLeaseTerm1',
    'I-OperatingLeaseWeightedAverageRemainingLeaseTerm1',
    'B-OperatingLeasesRentExpenseNet',
    'B-OperatingLossCarryforwards',
    'B-PaymentsToAcquireBusinessesGross',
    'B-PaymentsToAcquireBusinessesNetOfCashAcquired',
    'B-PreferredStockDividendRatePercentage',
    'B-PreferredStockSharesAuthorized',
    'I-PreferredStockSharesAuthorized',
    'B-ProceedsFromIssuanceOfCommonStock',
    'B-PropertyPlantAndEquipmentUsefulLife',
    'I-PropertyPlantAndEquipmentUsefulLife',
    'B-PublicUtilitiesRequestedRateIncreaseDecreaseAmount',
    'B-RelatedPartyTransactionAmountsOfTransaction',
    'I-RelatedPartyTransactionAmountsOfTransaction',
    'B-RelatedPartyTransactionExpensesFromTransactionsWithRelatedParty',
    'I-RelatedPartyTransactionExpensesFromTransactionsWithRelatedParty',
    'B-RepaymentsOfDebt',
    'B-RestructuringAndRelatedCostExpectedCost1',
    'B-RestructuringCharges',
    'B-RevenueFromContractWithCustomerExcludingAssessedTax',
    'B-RevenueFromContractWithCustomerIncludingAssessedTax',
    'B-RevenueFromRelatedParties',
    'B-RevenueRemainingPerformanceObligation',
    'B-Revenues',
    'B-SaleOfStockNumberOfSharesIssuedInTransaction',
    'I-SaleOfStockNumberOfSharesIssuedInTransaction',
    'B-SaleOfStockPricePerShare',
    'B-ShareBasedCompensation',
    'B-ShareBasedCompensationArrangementByShareBasedPaymentAwardAwardVestingPeriod1',
    'I-ShareBasedCompensationArrangementByShareBasedPaymentAwardAwardVestingPeriod1',
    'B-ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriod',
    'I-ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriod',
    'B-ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriodWeightedAverageGrantDateFairValue',
    'B-ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedNumber',
    'B-ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriodTotalFairValue',
    'B-ShareBasedCompensationArrangementByShareBasedPaymentAwardNumberOfSharesAuthorized',
    'I-ShareBasedCompensationArrangementByShareBasedPaymentAwardNumberOfSharesAuthorized',
    'B-ShareBasedCompensationArrangementByShareBasedPaymentAwardNumberOfSharesAvailableForGrant',
    'B-ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsExercisesInPeriodTotalIntrinsicValue',
    'B-ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsGrantsInPeriodGross',
    'B-ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsGrantsInPeriodWeightedAverageGrantDateFairValue',
    'B-SharePrice',
    'B-SharebasedCompensationArrangementBySharebasedPaymentAwardAwardVestingRightsPercentage',
    'I-SharebasedCompensationArrangementBySharebasedPaymentAwardAwardVestingRightsPercentage',
    'B-SharebasedCompensationArrangementBySharebasedPaymentAwardExpirationPeriod',
    'I-SharebasedCompensationArrangementBySharebasedPaymentAwardExpirationPeriod',
    'B-StockIssuedDuringPeriodSharesNewIssues',
    'I-StockIssuedDuringPeriodSharesNewIssues',
    'B-StockRepurchaseProgramAuthorizedAmount1',
    'B-StockRepurchaseProgramRemainingAuthorizedRepurchaseAmount1',
    'B-StockRepurchasedAndRetiredDuringPeriodShares',
    'B-StockRepurchasedDuringPeriodShares',
    'I-StockRepurchasedDuringPeriodShares',
    'B-SupplementalInformationForPropertyCasualtyInsuranceUnderwritersPriorYearClaimsAndClaimsAdjustmentExpense',
    'B-TreasuryStockAcquiredAverageCostPerShare',
    'B-TreasuryStockSharesAcquired',
    'I-TreasuryStockSharesAcquired',
    'B-TreasuryStockValueAcquiredCostMethod',
    'B-UnrecognizedTaxBenefits',
    'B-UnrecognizedTaxBenefitsThatWouldImpactEffectiveTaxRate',
    'I-DeferredFinanceCostsGross',
    'I-CommonStockParOrStatedValuePerShare',
    'I-LossContingencyEstimateOfPossibleLoss',
    'I-DefinedContributionPlanCostRecognized',
    'I-DebtInstrumentFairValue',
    'I-ContractWithCustomerLiabilityRevenueRecognized',
    'I-RevenueRemainingPerformanceObligation',
    'I-EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognized',
    'I-DebtInstrumentInterestRateStatedPercentage',
    'I-OperatingLossCarryforwards',
    'I-MinorityInterestOwnershipPercentageByNoncontrollingOwners',
    'I-InterestExpense',
    'I-LongTermDebt',
    'I-ShareBasedCompensation',
    'I-DebtWeightedAverageInterestRate',
    'I-DebtInstrumentCarryingAmount',
    'I-DebtInstrumentConvertibleConversionPrice1',
    'I-IncomeTaxExpenseBenefit',
    'I-ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsGrantsInPeriodWeightedAverageGrantDateFairValue',
    'I-EmployeeServiceShareBasedCompensationNonvestedAwardsTotalCompensationCostNotYetRecognizedShareBasedAwardsOtherThanOptions',
    'I-EquityMethodInvestments',
    'I-DebtInstrumentUnamortizedDiscount',
    'I-GainsLossesOnExtinguishmentOfDebt',
    'I-ShareBasedCompensationArrangementByShareBasedPaymentAwardNumberOfSharesAvailableForGrant',
    'I-BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedIntangibleAssetsOtherThanGoodwill',
    'I-PreferredStockDividendRatePercentage',
    'I-RevenueFromContractWithCustomerIncludingAssessedTax',
    'I-OperatingLeaseWeightedAverageDiscountRatePercent',
    'I-LineOfCredit',
    'I-LineOfCreditFacilityMaximumBorrowingCapacity',
    'I-EffectiveIncomeTaxRateReconciliationAtFederalStatutoryIncomeTaxRate',
    'I-LineOfCreditFacilityCommitmentFeePercentage',
    'I-BusinessCombinationConsiderationTransferred1',
    'I-CommonStockDividendsPerShareDeclared',
    'I-DebtInstrumentBasisSpreadOnVariableRate1',
    'I-DisposalGroupIncludingDiscontinuedOperationConsideration',
    'I-ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsGrantsInPeriodGross',
    'I-CommonStockSharesOutstanding',
    'I-AmortizationOfFinancingCosts',
    'I-LineOfCreditFacilityCurrentBorrowingCapacity',
    'I-TreasuryStockValueAcquiredCostMethod',
    'I-ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsNonvestedNumber',
    'I-DebtInstrumentInterestRateEffectivePercentage',
    'I-SaleOfStockPricePerShare',
    'I-CapitalizedContractCostAmortization',
    'I-RestructuringCharges',
    'I-ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsVestedInPeriodTotalFairValue',
    'I-AccrualForEnvironmentalLossContingencies',
    'I-CashAndCashEquivalentsFairValueDisclosure',
    'I-ProceedsFromIssuanceOfCommonStock',
    'I-Revenues',
    'I-BusinessCombinationRecognizedIdentifiableAssetsAcquiredAndLiabilitiesAssumedIntangibles',
    'I-LettersOfCreditOutstandingAmount',
    'I-ShareBasedCompensationArrangementByShareBasedPaymentAwardEquityInstrumentsOtherThanOptionsGrantsInPeriodWeightedAverageGrantDateFairValue',
    'I-OperatingLeasePayments',
    'I-LineOfCreditFacilityRemainingBorrowingCapacity',
    'I-PaymentsToAcquireBusinessesGross',
    'I-TreasuryStockAcquiredAverageCostPerShare',
    'I-DeferredFinanceCostsNet',
    'I-StockRepurchaseProgramAuthorizedAmount1',
    'I-InterestExpenseDebt',
    'I-ContractWithCustomerLiability',
    'I-OperatingLeaseExpense',
    'I-Depreciation',
    'I-AllocatedShareBasedCompensationExpense',
    'I-LossContingencyAccrualAtCarryingValue',
    'I-LineOfCreditFacilityUnusedCapacityCommitmentFeePercentage',
    'I-SupplementalInformationForPropertyCasualtyInsuranceUnderwritersPriorYearClaimsAndClaimsAdjustmentExpense',
    'I-OperatingLeaseLiability',
    'I-RevenueFromRelatedParties',
    'I-PaymentsToAcquireBusinessesNetOfCashAcquired',
    'I-BusinessCombinationContingentConsiderationLiability',
    'I-LossContingencyDamagesSoughtValue',
    'I-NumberOfOperatingSegments',
    'I-BusinessAcquisitionEquityInterestsIssuedOrIssuableNumberOfSharesIssued',
    'I-OperatingLeaseRightOfUseAsset',
    'I-BusinessCombinationAcquisitionRelatedCosts',
    'I-UnrecognizedTaxBenefits',
    'I-GuaranteeObligationsMaximumExposure',
    'I-RestructuringAndRelatedCostExpectedCost1',
    'I-DefinedBenefitPlanContributionsByEmployer',
    'I-OperatingLeaseCost',
    'I-DerivativeFixedInterestRate',
    'I-Goodwill',
    'I-GoodwillImpairmentLoss',
    'I-CommonStockCapitalSharesReservedForFutureIssuance',
    'I-StockRepurchasedAndRetiredDuringPeriodShares',
    'I-EmployeeServiceShareBasedCompensationTaxBenefitFromCompensationExpense',
    'I-IncomeLossFromEquityMethodInvestments',
    'I-NumberOfReportableSegments',
    'I-LongTermDebtFairValue',
    'I-RepaymentsOfDebt',
    'I-ConcentrationRiskPercentage1',
    'I-DebtInstrumentRedemptionPricePercentage',
    'I-CumulativeEffectOfNewAccountingPrincipleInPeriodOfAdoption',
    'I-SharePrice',
    'I-UnrecognizedTaxBenefitsThatWouldImpactEffectiveTaxRate',
    'I-ShareBasedCompensationArrangementByShareBasedPaymentAwardOptionsExercisesInPeriodTotalIntrinsicValue',
    'I-EffectiveIncomeTaxRateContinuingOperations',
    'I-RevenueFromContractWithCustomerExcludingAssessedTax',
    'I-StockRepurchaseProgramRemainingAuthorizedRepurchaseAmount1',
    'I-LineOfCreditFacilityInterestRateAtPeriodEnd',
    'I-ClassOfWarrantOrRightExercisePriceOfWarrantsOrRights1',
    'I-OperatingLeasesRentExpenseNet',
    'I-LeaseAndRentalExpense',
    'I-PublicUtilitiesRequestedRateIncreaseDecreaseAmount',
    'I-MinorityInterestOwnershipPercentageByParent',
    'I-AssetImpairmentCharges',
    'I-DerivativeNotionalAmount']
    for i in output:
        output_name.append(names[int(i)])
    print(output)
    return render_template('index.html', submitted_text=output_name)


def predict_custom_trained_model(
    project: str,
    endpoint_id: str,
    instances: Union[Dict, List[Dict]],
    location: str = "us-east1",
    api_endpoint: str = "us-east1-aiplatform.googleapis.com",
):
    """Make a prediction to a deployed custom trained model
    Args:
        project (str): Project ID
        endpoint_id (str): Endpoint ID
        instances (Union[Dict, List[Dict]]): Dictionary containing instances to predict
        location (str, optional): Location. Defaults to "us-east1".
        api_endpoint (str, optional): API Endpoint. Defaults to "us-east1-aiplatform.googleapis.com".
    """
    
    # The AI Platform services require regional API endpoints.
    client_options = {"api_endpoint": api_endpoint}
    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.
    client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)
    # The format of each instance should conform to the deployed model's prediction input schema.
    instances = instances if isinstance(instances, list) else [instances]
    instances = [
        json_format.ParseDict(instance_dict, Value()) for instance_dict in instances
    ]
    parameters_dict = {}
    parameters = json_format.ParseDict(parameters_dict, Value())
    endpoint = client.endpoint_path(
        project=project, location=location, endpoint=endpoint_id
    )
    response = client.predict(
        endpoint=endpoint, instances=instances, parameters=parameters
    )
    print("response")
    print(" deployed_model_id:", response.deployed_model_id)
    # The predictions are a google.protobuf.Value representation of the model's predictions.
    predictions = response.predictions
    return predictions
    # for prediction in predictions:
    #     print("prediction:", dict(prediction))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
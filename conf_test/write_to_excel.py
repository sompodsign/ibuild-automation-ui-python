import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils import excel_utils
from utils.CompanyDataConfigForExcel import *
import pathlib
from uuid import uuid4
from conf_test.testData_configuration_for_run_test import File_Name_of_the_instance


def writetoToExcel():
    addProductData = [productName, primaryNumber, categoryName, categoryDesc, linkedToProduct,
                      subCategoryName, subCategoryDesc, linkedToCat, articleName, articleDesc, linkedTosubCat]
    clientPath = pathlib.Path(__file__).parent / f"../TestData/{File_Name_of_the_instance}"
    rowsAddCompany = ExcelUtils.getRowCount(clientPath, sheetNameForCompany)
    rowsAddContacts = ExcelUtils.getRowCount(clientPath, sheetNameForContact)
    rowsAddIP = ExcelUtils.getRowCount(clientPath, sheetNameForIP)
    rowsAddProducts = ExcelUtils.getRowCount(clientPath, sheetNameForProduct)
    columnsAddProduct = ExcelUtils.getColCount(clientPath, sheetNameForProduct)
    print(type(columnsAddProduct))

    companyNameList = []
    # adding Company through this code
    for r in range(2, rowsAddCompany + 1):
        unique_id = str(uuid4())[:8]
        businessCategoryName = ExcelUtils.readData(clientPath, sheetNameForCompany, r, 2)
        ExcelUtils.writeData(clientPath, sheetNameForCompany, r, 1, id + " " + str(businessCategoryName) + " " + name + " " + unique_id)
        ExcelUtils.writeData(clientPath, sheetNameForCompany, r, 6, 0)
        nameOfCompany = ExcelUtils.readData(clientPath, sheetNameForCompany, r, 1)
        companyNameList.append(nameOfCompany)

    print(companyNameList)
    start = 0

    # Adding IP Data
    for rowIp in range(2, rowsAddIP + 1):
        unique_id = str(uuid4())[:8]
        ExcelUtils.writeData(clientPath, sheetNameForIP, rowIp, 2, ipName + " " + unique_id)
        ExcelUtils.writeData(clientPath, sheetNameForIP, rowIp, 3, ipPrimaryId + " " + unique_id)
        start = start + 1
        if start <= len(companyNameList):
            for n in range(start, len(companyNameList) + 1):

                if matchSubStringForLicensorCompany in companyNameList[n - 1]:
                    ExcelUtils.writeData(clientPath, sheetNameForIP, rowIp, 1, companyNameList[n - 1])
                    ExcelUtils.writeData(clientPath, sheetNameForIP, rowIp, 7, 0)
                    break
                else:
                    for n in companyNameList:
                        if matchSubStringForLicensorCompany in n:
                            ExcelUtils.writeData(clientPath, sheetNameForIP, rowIp, 1, n)
                            ExcelUtils.writeData(clientPath, sheetNameForIP, rowIp, 7, 0)

    # Adding Contacts Data
    for rowContact in range(2, rowsAddContacts + 1):
        rolesForContact = str(ExcelUtils.readData(clientPath, sheetNameForContact, rowContact, 5))
        hintOfUserCompany = str(ExcelUtils.readData(clientPath, sheetNameForContact, rowContact, 7))
        unique_id = str(uuid4())[:8]
        if rolesForContact == roleLicensor:
            ExcelUtils.writeData(clientPath, sheetNameForContact, rowContact, 3, lastNameContactLicensor + " " + unique_id)
        elif rolesForContact == roleLicenseeRoyalty:
            ExcelUtils.writeData(clientPath, sheetNameForContact, rowContact, 3, lastNameContactLicenseeRoyalty + " " + unique_id)
        elif rolesForContact == roleAgent:
            ExcelUtils.writeData(clientPath, sheetNameForContact, rowContact, 3, lastNameContactAgent + " " + unique_id)
        elif rolesForContact == roleLicensee:
            ExcelUtils.writeData(clientPath, sheetNameForContact, rowContact, 3, lastNameContactLicensee + " " + unique_id)

        # if test_data.clientID == 2:
        if matchSubStringForLicensorCompany in hintOfUserCompany:
            for n in companyNameList:
                if matchSubStringForLicensorCompany in n:
                    ExcelUtils.writeData(clientPath, sheetNameForContact, rowContact, 7, n)
                    ExcelUtils.writeData(clientPath, sheetNameForContact, rowContact, 9, 0)
                    break
        elif matchSubStringForLicenseeCompany in hintOfUserCompany:
            for n in companyNameList:
                if matchSubStringForLicenseeCompany in n:
                    ExcelUtils.writeData(clientPath, sheetNameForContact, rowContact, 7, n)
                    ExcelUtils.writeData(clientPath, sheetNameForContact, rowContact, 9, 0)
                    break
        elif matchSubStringForAgentCompany in hintOfUserCompany:
            for n in companyNameList:
                if matchSubStringForAgentCompany in n:
                    ExcelUtils.writeData(clientPath, sheetNameForContact, rowContact, 7, n)
                    ExcelUtils.writeData(clientPath, sheetNameForContact, rowContact, 9, 0)
                    break

    for r in range(2, rowsAddProducts + 1):
        unique_id = str(uuid4())[:8]
        for col in range(1, (columnsAddProduct - 1) + 1):
            ExcelUtils.writeData(clientPath, sheetNameForProduct, r, col, addProductData[col - 1] + " " + unique_id)
        ExcelUtils.writeData(clientPath, sheetNameForProduct, r, 12, 0)


writetoToExcel()

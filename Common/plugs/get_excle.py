from openpyxl import load_workbook


class DoExcle:

    def __init__(self, filename, sheetname):
        self.filename = filename
        self.sheetname = sheetname

    def read_data(self):
        test_data = []
        wb = load_workbook(self.filename)
        sheet = wb[self.sheetname]

        for i in range(2, sheet.max_row + 1):
            row_data = {}
            row_data['sheetname'] = self.sheetname
            row_data['id'] = sheet.cell(i, 1).value
            row_data['level'] = sheet.cell(i, 2).value
            row_data['description'] = sheet.cell(i, 3).value
            row_data['method'] = sheet.cell(i, 4).value
            row_data['url'] = sheet.cell(i, 5).value
            row_data['parm'] = sheet.cell(i, 6).value
            row_data['excepted'] = sheet.cell(i, 7).value
            row_data['sql'] = sheet.cell(i, 8).value
            test_data.append(row_data)
        return test_data

    def write_data(self, sheetname, row, col, value):
        wb = load_workbook(self.filename)
        sheet = wb[sheetname]
        sheet.cell(row, col).value = value
        wb.save(self.filename)


def split_list(lst, n=3):
    data_split_list = [[] for x in range(n)]
    [data_split_list[0].append(i) for i in lst if i['level'] == 'P1']
    [data_split_list[1].append(i) for i in lst if i['level'] == 'P2']
    [data_split_list[2].append(i) for i in lst if i['level'] == 'P3']
    return data_split_list


if __name__ == '__main__':
    DE = DoExcle('../../TestData/case.xlsx', 'user')
    caseList = split_list(DE.read_data())
    print(caseList[0])
    print(caseList[0][0]['sql'])

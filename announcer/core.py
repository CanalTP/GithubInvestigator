import logging
import xlsxwriter

class Core(object):
    workbook = None
    worksheet = None

    def column_title_format(self):
        format = self.workbook.add_format()
        format.set_align('center')
        format.set_bold()
        format.set_border()

        return format

    def is_format(self, condition):
        format = self.workbook.add_format()
        format.set_bg_color('green' if condition else 'red')
        format.set_align('center')
        format.set_border()

        return format

    def write_column_titles(self, report):
        col = 0

        self.worksheet.write(0, col, 'Github Repository', self.column_title_format())
        col += 1
        self.worksheet.write(0, col, 'Is public', self.column_title_format())
        col += 1
        self.worksheet.write(0, col, 'Fork', self.column_title_format())
        col += 1
        for fileName, isPresent in report.files.iteritems():
            self.worksheet.write(0, col, fileName, self.column_title_format())
            col += 1

        return

    def publish(self, reports, dest_path, file_name):
        path = dest_path + '/' + file_name + '.xlsx'
        self.workbook = xlsxwriter.Workbook(path)
        self.worksheet = self.workbook.add_worksheet()
        self.worksheet.set_column('A:A', 30)
        row = 1

        self.write_column_titles(reports[0])
        for repo in reports:
            col = 0

            self.worksheet.write(row, col, repo.name)
            col += 1
            self.worksheet.write(row, col, repo.is_public, self.is_format(repo.is_public))
            col += 1
            self.worksheet.write(row, col, repo.is_fork, self.is_format(repo.is_fork))
            col += 1
            for name, isPresent in repo.files.iteritems():
                self.worksheet.write_boolean(row, col, isPresent, self.is_format(isPresent))
                col += 1
            row += 1

        self.workbook.close()
        logging.info('File path: ' + path)

        return

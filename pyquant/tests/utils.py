import pyclbr
import os


def test_all_file_from_inspection(module):
    rlt = pyclbr.readmodule(module)
    for key, value in rlt.items():
        print 'trying ' + key
        full_path = value.file
        file_name = os.path.basename(full_path)
        dir_name = os.path.dirname(full_path)

        test_dir = os.path.join(dir_name, 'tests')
        if os.path.exists(test_dir):
            test_file = os.path.join(test_dir, 'test_' + file_name)
            if os.path.exists(test_file):

                print 'import ' + test_file

if __name__ == '__main__':
    test_all_file_from_inspection('pyquant.instrument.single_range_accrual')
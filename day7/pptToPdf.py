#
#
#
#

import comtypes

try:
    import comtypes.client
except Exception as e:
    print(e)
import os


def init_powerpoint():
    """"""
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = 1
    return powerpoint


def ppt_to_pdf(powerpoint, inputFileName, outputFileName, formatType=32):
    """"""
    if outputFileName[-3:] != 'pdf' or outputFileName[-3:] != 'PDF':
        outputFileName += '.pdf'
    deck = powerpoint.Presentaions.Open(inputFileName)
    deck.SaveAs(outputFileName, formatType)
    deck.Close()


def convert_files_in_folder(powerpoint, cwd, scanFolder):
    """"""
    files = os.listdir(scanFolder)
    pptfiles = [f for f in files if f.endswith(("ppt", "pptx"))]
    for pptfile in pptfiles:
        pptfilefullpath = os.path.join(cwd, pptfile)
        ppt_to_pdf(powerpoint, pptfilefullpath, pptfilefullpath)


def paramsInputAndDoneFunc():
    """"""
    # /Users/wangxiaolong/Desktop/
    scanFolder = str(input("请输入扫描文件夹："))
    powerpoint = init_powerpoint()
    cwd = os.getcwd()
    convert_files_in_folder(powerpoint, scanFolder, scanFolder)
    powerpoint.Quit()


if __name__ == '__main__':
    try:
        paramsInputAndDoneFunc()
    except Exception as e:
        print(e)

import KeyphraceExtraction
import GetDiscription_Bot


def main(UsrName= 'technologyreview'):
    ################## MOVE EXTRACTED CAPTION HERE ####################
    document = GetDiscription_Bot.main(UsrName=UsrName)

    ################## GET EXTRACTED KEYPHRACES
    key_phraces = KeyphraceExtraction.main(document=document)
    return key_phraces

if __name__ == '__main__':
    main()
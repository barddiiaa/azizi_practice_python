v = float(input("sorat bad ra vared knid:"))
T = float(input("dama ra wared knid:"))
wind_child = 13.13 + (0.62 * T) - (13.95 * v) + (0.486 * T * v)
print(f"vazesh bad:{wind_child}")

import re
def decrypt_clue(text):

    pattern = r'\b(?:list|int|def|class|return|try|except|for|from|import|global|if|else|lambda|nonlocal|pass|raise|while|with|and|or|assert|break|continue|finally)\b'

    keywords = re.findall(pattern, text)

    print("کلمات کلیدی پایتون در متن:")
    for keyword in keywords:
        print(keyword)


text = "ThereareyouIandletlistintgameJupiterlinedefblindasyieldassertbreakclasscontinueexceptfinallyforfromglobalimportnonlocalpassraisereturntrywhilewithandorasassertbreakclasscontinuedefdelelifelseexceptexecfinallyforfromglobalifimportinislambdnonlocalnotorpassprintraisereprreturnsupertrywhilewithyieldTrueFalseNoneasyncawaitmatchcasenonelocaloverrideprivatesealedstaticmethodvolatileabstractenumintfloatdoublebyteboolcharstructvectorlistdictionaryqueuestackinterfacenulltrycatchfinallythrowthrowsimplementsextendspublicprotectedprivatefinalstaticvoidmainStringargsSystemoutprintlnnewMapSetGetAddRemoveClearIsEmptySizeContainsKeyContainsValueKeyValuePairsForEachDoWhileSwitchCaseDefaultbreakcontinueiteratoriterablecollectionsframeworksynchronizedtransientvolatilestrictfpbitwiselogicalshiftcompoundassignmenttypeinferencegenericswildcardstypeerasurereflectionproxydecoratorfactorysingletonprototypebuildercompositeadapterbridgechainofresponsibilitycommandstateobservermementointerpreteriteratorvisitorstrategytemplatemethodflyweightmediatorproxymultithreadingconcurrencyasynchronousprogrammingeventdrivenarchitecturefunctionalprogrammingimmutables..."
decrypt_clue(text)

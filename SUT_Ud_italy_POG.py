"file names"
dataFileName = 'SUT_Ud_italy_DATA.xlsx'
scenarioFileName = 'Inventory.xlsx'
resultsFileName = 'Results.xlsx'

# fundamental data
nYRS = 64 # time scope
nOBJ = 80 # objects included in impact assessment

"dictionaries structure"
y = [str(x) for x in np.arange(1,nYRS+1)]    # YEARS: time scope of the analysis
s = ['bau','pog']                            # SCENARIO: business as usual, polimi open ground
l = ['eco','ene']                            # LAYERS: (reference l is the first one), eco:M€, ene:TJ, (mas:kton)
p = ['CO','OP']                              # PHASES: construction, operation

"unit of measure"
unit = [1, 1, 1]  # M€,TJ,kton (if the given UoM are not ideal, insert appropriate multipliers to convert them)
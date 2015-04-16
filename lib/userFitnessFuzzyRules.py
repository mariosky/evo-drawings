__author__ = 'Jc Romero'

from FIS import *

preference = LinguisticVariable('preference', range=(0.0, 5.0))
preference.addMF('Low',MF.Triangular(-2, 1, 3))
preference.addMF('Mid',MF.Triangular(2.5, 3, 4.5))
preference.addMF('High',MF.Triangular(3, 5, 5))

activity = LinguisticVariable('experience', range=(0.0, 100.0))
activity.addMF('Low',MF.Triangular(1, 1, 50))
activity.addMF('Mid',MF.Triangular(30, 50, 70))
activity.addMF('High',MF.Triangular(50, 100, 100 ))

#OUT
Out = LinguisticVariable('fitness', type='out', range=(0.0, 100.0))
Out.addMF('Bad',MF.Triangular(-2, 1, 50))
Out.addMF('Normal',MF.Triangular(30, 50, 70))
Out.addMF('Good',MF.Triangular(50, 100, 100 ))


# Rules
#if preferance is low and activity is low then fitness is bad
r1 = FuzzyRule()
r1.antecedent.append(FuzzyOperator('and',FuzzyProposition(preference,preference.mfs['Low']),FuzzyProposition(activity,activity.mfs['Low'])))
r1.consequent.append(FuzzyProposition(Out,Out.mfs['Bad']))

#if preferance is low and activity is mid then fitness is bad
r2 = FuzzyRule()
r2.antecedent.append(FuzzyOperator('and',FuzzyProposition(preference,preference.mfs['Low']),FuzzyProposition(activity,activity.mfs['Mid'])))
r2.consequent.append(FuzzyProposition(Out,Out.mfs['Bad']))

#if preferance is low and activity is high then fitness is normal
r3 = FuzzyRule()
r3.antecedent.append(FuzzyOperator('and',FuzzyProposition(preference,preference.mfs['Low']),FuzzyProposition(activity,activity.mfs['High'])))
r3.consequent.append(FuzzyProposition(Out,Out.mfs['Normal']))

#if preferance is mid and activity is low then fitness is bad
r4 = FuzzyRule()
r4.antecedent.append(FuzzyOperator('and',FuzzyProposition(preference,preference.mfs['Mid']),FuzzyProposition(activity,activity.mfs['Low'])))
r4.consequent.append(FuzzyProposition(Out,Out.mfs['Bad']))

#if preferance is mid and activity is mid then fitness is normal
r5 = FuzzyRule()
r5.antecedent.append(FuzzyOperator('and',FuzzyProposition(preference,preference.mfs['Mid']),FuzzyProposition(activity,activity.mfs['Mid'])))
r5.consequent.append(FuzzyProposition(Out,Out.mfs['Normal']))

#if preferance is mid and activity is high then fitness is normal
r6 = FuzzyRule()
r6.antecedent.append(FuzzyOperator('and',FuzzyProposition(preference,preference.mfs['Mid']),FuzzyProposition(activity,activity.mfs['High'])))
r6.consequent.append(FuzzyProposition(Out,Out.mfs['Good']))

#if preferance is high and activity is low then fitness is good
r7 = FuzzyRule()
r7.antecedent.append(FuzzyOperator('and',FuzzyProposition(preference,preference.mfs['High']),FuzzyProposition(activity,activity.mfs['Low'])))
r7.consequent.append(FuzzyProposition(Out,Out.mfs['Normal']))

#if preferance is high and activity is mid then fitness is good
r8 = FuzzyRule()
r8.antecedent.append(FuzzyOperator('and',FuzzyProposition(preference,preference.mfs['High']),FuzzyProposition(activity,activity.mfs['Mid'])))
r8.consequent.append(FuzzyProposition(Out,Out.mfs['Good']))

#if preferance is high and activity is high then fitness is good
r9 = FuzzyRule()
r9.antecedent.append(FuzzyOperator('and',FuzzyProposition(preference,preference.mfs['High']),FuzzyProposition(activity,activity.mfs['High'])))
r9.consequent.append(FuzzyProposition(Out,Out.mfs['Good']))

Rules=[r1,r2,r3,r4,r5,r6,r7,r8,r9]
fis = FIS(Rules)


def fisuser(a,b):
    preference.current_value=a
    activity.current_value=b
    return fis.eval( out_var = 0)

if __name__ == '__main__':
    print eval(25,15)

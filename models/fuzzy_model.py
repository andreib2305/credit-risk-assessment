import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

class FuzzyRiskEval:

    def __init__(self):
        self.income = ctrl.Antecedent(np.arange(30000, 200000, 1000), 'income')
        self.late_payments = ctrl.Antecedent(np.arange(0, 8, 1), 'late_payments')
        self.risk = ctrl.Consequent(np.arange(0, 101, 1), 'risk')

        self.simulation = None
        self.setup_levels()
        self.setup_rules()

    def setup_levels(self):
        # Уровни дохода
        self.income['low'] = fuzz.trimf(self.income.universe, [30000, 30000, 80000])
        self.income['medium'] = fuzz.trimf(self.income.universe, [60000, 100000, 150000])
        self.income['high'] = fuzz.trimf(self.income.universe, [130000, 199000, 199000])

        # Уровни просрочек
        self.late_payments['low'] = fuzz.trimf(self.late_payments.universe, [0, 0, 2])
        self.late_payments['medium'] = fuzz.trimf(self.late_payments.universe, [1, 3, 5])
        self.late_payments['high'] = fuzz.trimf(self.late_payments.universe, [4, 7, 7])

        # Уровень риска
        self.risk['low'] = fuzz.trimf(self.risk.universe, [0, 0, 50])
        self.risk['high'] = fuzz.trimf(self.risk.universe, [50, 100, 100])

    def setup_rules(self):
        rule1 = ctrl.Rule(self.income['low'] & self.late_payments['high'], self.risk['high'])
        rule2 = ctrl.Rule(self.income['high'] & self.late_payments['low'], self.risk['low'])
        rule3 = ctrl.Rule(self.late_payments['high'], self.risk['high'])
        rule4 = ctrl.Rule(self.income['low'] & self.late_payments['medium'], self.risk['high'])
        rule5 = ctrl.Rule(self.income['high'] & self.late_payments['medium'], self.risk['low'])

        risk_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
        self.simulation = ctrl.ControlSystemSimulation(risk_ctrl)

    def eval(self, income_val: float, late_payments_val: int) -> tuple[float, int]:
        self.simulation.input['income'] = income_val
        self.simulation.input['late_payments'] = late_payments_val

        self.simulation.compute()

        risk_score = self.simulation.output['risk']
        risk_class = 1 if risk_score >= 50 else 0

        return risk_score, risk_class

def dataFromPDF(question):
    data = [
        {
            'Smart Protect Goal Brochure':{
                "What are the various options under Life Cover Variant?": 'The following options are\n\
                \u2022 Whole of Life Life Cover up to age 99 years : This option is only available when limited premium payment option is chosen\n\
                \u2022 Return of Premiums (ROP) If no claim has been made for the Variant and/or for each Add-on cover(s), the total premiums paid for the Variant and/or each of the Add-on cover(s) opted for, will be returned on their respective maturity dates. If Whole Life is opted, ROP will not be available.',

                "What are the Add-on covers options under Variant description Life Cover?":'The following Add-on covers\n\
                \u2022 Accidental Death Benefit (ADB): In case of death due to an accident, Sum Assured chosen as ADB is payable.\n\
                \u2022 Accidental Total Permanent Disability Benefit (ATPDB): In case of occurrence of total permanent disability of the Life Assured due to an accident, Sum Assured chosen as ATPDB is payable.\n\
                \u2022 Critical Illness Benefit (CIB):\n\
                    \u2022 In case of diagnosis of any of the listed Critical Illnesses, Sum Assured chosen for Critical Illness benefit is payable.\n\
                    \u2022 In case of Minor CI other than Angioplasty, 25% of the CIB will be payable.\n\
                    \u2022 For Angioplasty, lower of 5 lakhs or 25% of CIB will be payable.\n\
                    \u2022 A maximum of four (4) Minor CI including Angioplasty claims will be payable during the CIB cover period.\n\
                    \u2022 For Major CI, 100% of CIB will be payable.',

                "What is the total claim covered under Minor and Major CI?":"The total claims paid under Minor and Major CI will not be more than 100% of CIB",

                "What is Waiver of Premium Benefit on CI?":"On occurrence of fourth (4 ) Minor CI or on the date of occurrence of the first (1st) Major CI (incl. ATPD), whichever is earlier, all future premiums due under the policy will be waived and WOPB-I cover will terminate immediately and automatically.",

                "What is Annualized Premium under Life Cover Variant?":"Annualized Premium is the total premium/s payable in a policy year for a LP, RP and the single premium for an SP. The annualized premium is exclusive of extra premium, add-on covers and loadings for modal premiums, if any, and Total Premiums paid shall be equal to (Annualized Premium * number of years for which premiums have been paid)",

                "Does the ROP include GST?":"ROP is excluding GST/any other applicable tax levied, subject to changes in tax laws and any extra premium.",
                
                "Under what condition is Add-on Covers applicable?":"Add-on Covers will only be applicable, subject to the conditions, exclusions, waiting period, cooling period &survival period as applicable",
                "What is the duration period of premiums for CIB & WOPBI?":"The premiums for CIB &amp WOPB are guaranteed for a period of 5 years and reviewable for subsequent cover periods",
                "What is the maximum maturity age with ROP under the variant?":"The maximum maturity age is 75 years.",
                "What is the maximum maturity age with Whole Life under the variant?":"The maximum maturity age is 99 years."

            },
            'Future Wealth Gain Brochure':{

                "What is Future Wealth Gain plan?": 'Bajaj Allianz Life Future Wealth Gain is a non-participating, individual, life, unit-linked regular/limited premium payment endowment plan with two variants, “Wealth Plus” and “Wealth Plus Care”. Bajaj Allianz Life Future Wealth Gain plan offers the dual benefit of protection and growth to fulfil the dreams of your loved ones.',

                "If the customer has done a partial withdrawls, is he eligible for the Loyalty Additions/Fund Boosters?": 'Yes. Policyholder will receive Loyalty Addition/ Fund Boosters, provided the policy is in-force and all premiums have been paid.',

                "What are the steps to select the plan?":'Plan Working\n\
                                            Step 1: Choose from the two variants Wealth Plus and Wealth Plus Care\n\
                                            Step 2: Choose the premium you want to pay\n\
                                            Step 3: Choose the sum assured multiplier to decide your life cover\n\
                                            Step 4: Choose your policy term and premium payment term\n\
                                            Step 5: Choose the premium payment frequency\n\
                                            Step 6: Choose between the two portfolio strategies\n\
                                            Step 7: Choose the riders (optional and with rider charges applicable)\n\
                                            Note:\n\
                                            \u2022 The variant has to be chosen at the inception of the policy and cannot be changed subsequently.\n\
                                            \u2022 Applicable as per the minimum/maximum sum assured criteria. Please refer to the Eligibility Parameters',

                "What are the maturity benefits available in the wealth plus variant of this plan?":"On the maturity date, you will receive the Regular Premium Fund Value plus Top up Premium Fund Value",

                "How can one revive a discontinued policy?":'Revival\n A policy which has been discontinued due to non-payment of premiums can only be revived subject to following conditions:\n\
                            1. The Insurance Company receives the request for revival from you within 3 years from the date of first unpaid premium provided the policy is not terminated already\n\
                            2. You submit such information and documentation as may be requested by the Insurance Company at your own expense.\n\
                            3. The policy may be revived on the original policy terms & conditions, revised terms & conditions or disallowed revival, based on Board approved underwriting guidelines.\n\
                            4. On revival of the discontinued policy,\n \u2022 The policy will be revived restoring the risk cover, Loyalty Addition and Fund Booster.\n \u2022 All the due but unpaid premiums will be collected from you without charging any interest or fee.\n \u2022 The Discontinuance Value of the policy together with the amount of discontinuance/ surrender charge (without any interest) as deducted by the Insurance Company on the date of discontinuance of the policy, shall be restored to the chosen fund split into to the applicable Fund/s available as on the date of discontinuance, at their prevailing unit price.\n \u2022 The Premium Allocation Charge and Policy Administration Charge, as applicable, during the discontinuance period shall be deducted as applicable from regular premiums paid or from the fund at the time of revival.\n  \u2022 The Loyalty Additions due-but-not-allotted during the period the Policy was in Discontinuance shall be added to the Regular Premium Fund Value.',

                'What are the tax benefit options available under this policy?':'Tax Benefit \n\ Premium paid, maturity benefit, death benefit and surrender benefit are eligible for tax benefits as per extant Income Tax Act, subject to the provision stated therein and as amended from time to time.\n\ You are requested to consult your tax consultant and obtain independent advice for eligibility and before claiming any benefit under the policy.',

                'What are the features under "Wealth Plus" & "Wealth Plus Care" Variant?':'Bajaj Allianz Life Future Wealth Gain provides you with two unique portfolio strategies, which can be chosen at the inception of your policy or on any subsequent policy anniversary:\n\
                    a) Investor selectable Portfolio Strategy\n\ b) Wheel of Life Portfolio Strategy',
                    
                "Can I switch between the funds?":'Yes, there is an option to switch between funds - only under the Investor Selectable Portfolio Strategy.\n\
You have the flexibility to switch units between your investment funds according to your risk appetite and investment decisions, by giving written notice to the Insurance Company.\n\
\u2022 You can make unlimited free switches.\n\
\u2022 The minimum switching amount is Rs 5,000 or the value of units in the fund to be switched from, whichever is lower.\n\
\u2022 The Insurance Company shall effect the switch by redeeming units from the fund to be switched from and allocating new units in the fund being switched to at their respective unit price.'
            }
        }
    ]

    for brochure in data:
        if question in brochure['Smart Protect Goal Brochure']:
            return brochure['Smart Protect Goal Brochure'][question]
        elif question in brochure['Future Wealth Gain Brochure']:
            return brochure['Future Wealth Gain Brochure'][question]
    
    return "Answer not found in available data."

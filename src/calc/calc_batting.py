import math
from random import random

from data.constants import *


class BattingCalculator:
    StaticRandomInt1 = 7769  # <= 32767
    StaticRandomInt2 = 5359  # <= 32767
    USHORT_8089269c = 1828  # <= 32767
    inMemBatter = {}
    inMemPitcher = {}
    inMemBall = {}
    readValues = {}
    Hit_HorizontalAngle = 0
    Hit_VerticalAngle = 0
    Hit_HorizontalPower = 0
    AddedContactGravity = 0
    Display_Output = {}

    def floor(f):
        return math.trunc(f)

    def LinearInterpolateToNewRange(value, prevMin, prevMax, nextMin, nextMax):
        min = 0.0
        max = 0.0
        if (min == (prevMax - prevMin)):
            max = 1.0
        else:
            max = 1.0
            calcedValue = (value - prevMin) / (prevMax - prevMin)

            if ((calcedValue <= max)):
                max = calcedValue
                if (calcedValue < min):
                    max = min
        return (nextMax - nextMin) * max + nextMin

    def calculateContact(self):
        chargeUp = self.inMemBatter["BatterAtPlate_BatterCharge_Up"]
        contactSize = self.inMemBatter["Batter_SlapContactSize"]
        if (self.inMemBatter["AtBat_Mystery_CaptainStarSwing"] != 0):
            # if there was a star swing, make contact size 100
            chargeUp = 0.0
            contactSize = 100.0

        if (self.inMemBatter["Batter_IsBunting"] == False):
            if (chargeUp <= 0.0):
                # If not charging
                if (self.inMemBatter["RandomBattingFactors_ChemLinksOnBase"] != 0):
                    # If there are chem links on base, make the contact size larger
                    contactSize *= CONTACT_CHEM_LINK_MULTIPLIERS[
                        self.inMemBatter["RandomBattingFactors_ChemLinksOnBase"]]

            else:
                # else there is a charge
                contactSize = self.inMemBatter["Batter_ChargeContactSize"]

        else:
            # else bunting, use bunting contact size
            contactSize = self.inMemBatter["Batter_Bunting"]

        diffInX = self.inMemBatter["interstitialBallContact_X"] - self.inMemBatter["posX"]
        if (self.inMemBatter["AtBat_BatterHand"] == LEFTY):
            diffInX = -diffInX

        if (diffInX >= 0.0):
            self.inMemBatter["CalculatedBallPos"] = 100.0 * \
                                                    (diffInX /
                                                     BATTER_HITBOXES[self.inMemBatter["Batter_CharID"]][
                                                         "HorizontalRangeFar"]) + 100.0

        else:
            self.inMemBatter["CalculatedBallPos"] = - \
                (100.0 * (diffInX /
                          BATTER_HITBOXES[self.inMemBatter["Batter_CharID"]]["HorizontalRangeNear"]) - 100.0)

        if (self.inMemBatter["CalculatedBallPos"] < 0.0):
            self.inMemBatter["CalculatedBallPos"] = 0.0

        if (200.0 < self.inMemBatter["CalculatedBallPos"]):
            self.inMemBatter["CalculatedBallPos"] = 200.0

        # Higher is better, makes ranges larger
        contactSize = contactSize / 100.0
        # Contact sizes are only based on slap/charge and trimming, and AI
        big_Array = BALL_CONTACT_ARRAY_807B6294[self.inMemBatter["AtBat_TrimmedBat"]][
            self.inMemBatter["Batter_Contact_SlapChargeBuntStar"]][self.inMemBatter["EasyBatting"]]
        b0 = big_Array[0]
        b1 = big_Array[1]
        b2 = big_Array[2]
        b3 = big_Array[3]

        self.inMemBatter["LeftNiceThreshold"] = contactSize * (big_Array[4] - b0) + b0
        self.inMemBatter["LeftPerfectThreshold"] = contactSize * (big_Array[5] - b1) + b1
        self.inMemBatter["RightPerfectThreshold"] = contactSize * (big_Array[6] - b2) + b2
        self.inMemBatter["RightNiceThreshold"] = contactSize * (big_Array[7] - b3) + b3

        self.inMemBatter["Batter_ContactType"] = LEFT_SOUR
        if (self.inMemBatter["LeftNiceThreshold"] <= self.inMemBatter["CalculatedBallPos"]):
            self.inMemBatter["Batter_ContactType"] = LEFT_NICE

            if (self.inMemBatter["LeftPerfectThreshold"] <= self.inMemBatter["CalculatedBallPos"]):
                self.inMemBatter["Batter_ContactType"] = PERFECT

                if (self.inMemBatter["RightPerfectThreshold"] <= self.inMemBatter["CalculatedBallPos"]):
                    self.inMemBatter["Batter_ContactType"] = RIGHT_NICE

                    if (self.inMemBatter["RightNiceThreshold"] <= self.inMemBatter["CalculatedBallPos"]):
                        self.inMemBatter["Batter_ContactType"] = RIGHT_SOUR

        if (self.inMemBatter["Batter_ContactType"] == PERFECT):
            if (self.inMemBatter["CalculatedBallPos"] >= 100.0):
                self.inMemBatter["ContactQuality"] = 1.0 - (
                            self.inMemBatter["CalculatedBallPos"] - self.inMemBatter["LeftPerfectThreshold"]) / (
                                                             self.inMemBatter["RightPerfectThreshold"] -
                                                             self.inMemBatter["LeftPerfectThreshold"])

            else:
                self.inMemBatter["ContactQuality"] = (self.inMemBatter["CalculatedBallPos"] - self.inMemBatter[
                    "LeftPerfectThreshold"]) / (
                                                             self.inMemBatter["RightPerfectThreshold"] -
                                                             self.inMemBatter["LeftPerfectThreshold"])

            # if ((CONTACT_PERFECT_THRESHOLDS[self.inMemBatter["Batter_Contact_SlapChargeBuntStar"]][0] <= self.inMemBatter["CalculatedBallPos"]) and (self.inMemBatter["CalculatedBallPos"] <= CONTACT_PERFECT_THRESHOLDS[self.inMemBatter["Batter_Contact_SlapChargeBuntStar"]][1])):
            #     self.inMemBatter["mostPerfectContact"] = True

        elif (self.inMemBatter["Batter_ContactType"] < PERFECT):
            if (self.inMemBatter["Batter_ContactType"] == LEFT_SOUR):
                self.inMemBatter["ContactQuality"] = self.inMemBatter["CalculatedBallPos"] / \
                                                     self.inMemBatter["LeftNiceThreshold"]

            else:
                self.inMemBatter["ContactQuality"] = (self.inMemBatter["CalculatedBallPos"] - self.inMemBatter[
                    "LeftNiceThreshold"]) / (
                                                             self.inMemBatter["LeftPerfectThreshold"] -
                                                             self.inMemBatter["LeftNiceThreshold"])

        elif (self.inMemBatter["Batter_ContactType"] < RIGHT_SOUR):
            self.inMemBatter["ContactQuality"] = 1.0 - (
                        self.inMemBatter["CalculatedBallPos"] - self.inMemBatter["RightPerfectThreshold"]) / (
                                                         self.inMemBatter["RightNiceThreshold"] - self.inMemBatter[
                                                     "RightPerfectThreshold"])

        else:
            self.inMemBatter["ContactQuality"] = 1.0 - \
                                                 (self.inMemBatter["CalculatedBallPos"] - self.inMemBatter[
                                                     "RightNiceThreshold"]) / \
                                                 (200.0 - self.inMemBatter["RightNiceThreshold"])

        if (self.inMemBatter["AtBat_MoonShot"] != False):
            if (self.inMemBatter["Batter_ContactType"] == PERFECT):
                self.inMemBatter["AtBat_Mystery_CaptainStarSwing"] = 0

            else:
                self.inMemBatter["AtBat_MoonShot"] = False

        self.inMemBatter["Batter_HitType"] = -1
        if ((self.inMemBatter["Batter_Contact_SlapChargeBuntStar"] == SLAP) or (
                self.inMemBatter["Batter_Contact_SlapChargeBuntStar"] == CHARGE)):
            # Default to Sour
            self.inMemBatter["Batter_HitType"] = SOUR_CURVE_SLAP
            # Adjust if the hit was nice or perfect
            if (self.inMemBatter["Batter_ContactType"] == PERFECT):
                self.inMemBatter["Batter_HitType"] = PERFECT_CURVE_SLAP

            elif ((self.inMemBatter["Batter_ContactType"] == LEFT_NICE) or (
                    self.inMemBatter["Batter_ContactType"] == RIGHT_NICE)):
                self.inMemBatter["Batter_HitType"] = NICE_CURVE_SLAP

            # Adjust the HitType on a perfect pitch
            # 0xc for strike, 0xf for hit
            if (self.inMemPitcher["ChargePitchType"] == PITCHCHARGETYPE_PERFECT):
                if (self.inMemBatter["Batter_Contact_SlapChargeBuntStar"] == SLAP):
                    self.inMemBatter["Batter_HitType"] += SOUR_PERFECTPITCH_SLAP

                else:
                    self.inMemBatter["Batter_HitType"] += SOUR_PERFECTPITCH_CHARGE

            else:
                # Else not perfect charge pitch
                # If the pitch was Curve and contact was not a hit, it was a charge:
                # adjust by 0x3
                if (self.inMemPitcher["Pitcher_TypeOfPitch"] == PITCHCURVE):
                    if (self.inMemBatter["Batter_Contact_SlapChargeBuntStar"] != SLAP):
                        self.inMemBatter["Batter_HitType"] += SOUR_CURVE_CHARGE

                else:
                    # Else non-curve, which I believe is just a change up
                    # adjust by 0x6 for Hit
                    # adjust by 0x9 for Charge
                    if (self.inMemBatter["Batter_Contact_SlapChargeBuntStar"] == SLAP):
                        self.inMemBatter["Batter_HitType"] += SOUR_CHANGEUP_SLAP

                    else:
                        self.inMemBatter["Batter_HitType"] += SOUR_CHANGEUP_CHARGE

        self.Display_Output["Contact"] = {
            "DistanceFromPerfect": diffInX,
            "ContactZone": ["Left Sour", "Left Nice", "Perfect", "Right Nice", "Right Sour"][
                self.inMemBatter["Batter_ContactType"]],
            "ContactQuality": self.inMemBatter["ContactQuality"],
            "AbsoluteContact": self.inMemBatter["CalculatedBallPos"],
            "LeftNiceThreshold": self.inMemBatter["LeftNiceThreshold"],
            "LeftPerfectThreshold": self.inMemBatter["LeftPerfectThreshold"],
            "RightPerfectThreshold": self.inMemBatter["RightPerfectThreshold"],
            "RightNiceThreshold": self.inMemBatter["RightNiceThreshold"],
        }
        return

    def AdjustBallAngle(ballAngle):
        if (ballAngle < 0):
            while ballAngle < 0:
                ballAngle += 0x1000
        if (0xfff < ballAngle):
            while 0xfff < ballAngle:
                ballAngle += -0x1000
        return ballAngle

    def WeightedRandomIndex(self, vals, count):
        randomSum = 0

        loopSum = 0

        for element in vals:
            loopSum += element

        finSum = loopSum

        if (loopSum < 0):
            finSum = -loopSum

        if (finSum < 2):
            randomSum = 0

        else:
            # update RandomInt in case it's called successive times
            self.StaticRandomInt1 = (self.StaticRandomInt1 - (self.StaticRandomInt2 & 0xff)) + BattingCalculator.floor(
                self.StaticRandomInt2 / finSum) + self.USHORT_8089269c
            randomRange = self.StaticRandomInt1 - BattingCalculator.floor(self.StaticRandomInt1 / finSum) * finSum
            randomSum = (randomRange >> 0x1f ^ randomRange) - (randomRange >> 0x1f)
            if (loopSum < 0):
                randomSum = -randomSum

        p_loopArray = vals
        newIndex = 0
        i = 0
        if (0 < count):
            while (count != 0):
                if (randomSum < p_loopArray[i]):
                    return newIndex

                randomSum -= p_loopArray[i]
                newIndex += 1
                count += -1
                i += 1

        return 0

    def calculateBuntAngle(self):
        iVar3 = 0
        input = self.inMemBatter["ControllerInput"]

        contactType = self.inMemBatter["Batter_ContactType"]
        iVar2 = self.inMemBatter["Batter_SlapContactSize"] * (
                    BUNT_ANGLE_CALC_ARRAY[contactType][2] - BUNT_ANGLE_CALC_ARRAY[contactType][0])
        iVar1 = self.inMemBatter["Batter_SlapContactSize"] * (
                    BUNT_ANGLE_CALC_ARRAY[contactType][3] - BUNT_ANGLE_CALC_ARRAY[contactType][1])
        iVar2 = BattingCalculator.floor(iVar2 / 100) + (iVar2 >> 0x1f)
        iVar1 = BattingCalculator.floor(iVar1 / 100) + (iVar1 >> 0x1f)
        iVar2 = BUNT_ANGLE_CALC_ARRAY[contactType][0] + (iVar2 - (iVar2 >> 0x1f))
        iVar1 = (BUNT_ANGLE_CALC_ARRAY[contactType][1] + (iVar1 - (iVar1 >> 0x1f))) - iVar2
        iVar2 += self.StaticRandomInt1 - BattingCalculator.floor(self.StaticRandomInt1 / iVar1) * iVar1
        if (contactType != 0):
            if (contactType < 4):
                if (not input["Left"]):
                    if (not input["Right"]):
                        iVar3 = (self.StaticRandomInt2 & 1 ^ -(self.StaticRandomInt2 >> 0x1f)) + (
                                    self.StaticRandomInt2 >> 0x1f)
                    elif (self.inMemBatter["AtBat_BatterHand"] != RIGHTY):
                        iVar3 = 1
                elif (self.inMemBatter["AtBat_BatterHand"] == RIGHTY):
                    iVar3 = 1
        elif (contactType == 0):
            iVar3 = 1

        if (((self.inMemBatter["AtBat_BatterHand"] == RIGHTY) and (iVar3 != 0)) or (
        (self.inMemBatter["AtBat_BatterHand"] != RIGHTY and (iVar3 == 0)))):
            if (iVar2 < 0x801):
                iVar2 = 0x800 - iVar2
            else:
                iVar2 = 0x1800 - iVar2

        self.Hit_HorizontalAngle = BattingCalculator.AdjustBallAngle(iVar2)

        return

    def calculateBuntingExtras(self):
        uVar5 = ((self.StaticRandomInt1 & 1 ^ self.StaticRandomInt1 >> 0x1f) != self.StaticRandomInt1 >> 0x1f)
        uVar4 = self.inMemBatter["Batter_ContactType"]
        iVar6 = BUNTING_CONTACT_ARRAY[self.inMemBatter["Batter_ContactType"]][uVar5][0]
        iVar7 = BUNTING_CONTACT_ARRAY[uVar4][uVar5][1]
        iVar3 = self.inMemBatter["Batter_SlapContactSize"] * (BUNTING_CONTACT_ARRAY[uVar4][uVar5 + 2][0] - iVar6)
        iVar2 = self.inMemBatter["Batter_SlapContactSize"] * (BUNTING_CONTACT_ARRAY[uVar4][uVar5 + 2][1] - iVar7)
        iVar3 = BattingCalculator.floor(iVar3 / 100) + (iVar3 >> 0x1f)
        iVar2 = BattingCalculator.floor(iVar2 / 100) + (iVar2 >> 0x1f)
        iVar6 += iVar3 - (iVar3 >> 0x1f)
        iVar2 = (iVar7 + (iVar2 - (iVar2 >> 0x1f))) - iVar6
        Hit_VerticalAngle = iVar6 + (self.StaticRandomInt1 - (self.StaticRandomInt1 / iVar2) * iVar2)

        if (Hit_VerticalAngle < 0x401):
            if (Hit_VerticalAngle < -0x400):
                Hit_VerticalAngle += 0x1000
                Hit_HorizontalAngle = BattingCalculator.AdjustBallAngle(Hit_HorizontalAngle + 0x800)

            elif (Hit_VerticalAngle < 0):
                Hit_VerticalAngle += 0x1000
        else:
            Hit_VerticalAngle = 0x800 - Hit_VerticalAngle
            Hit_HorizontalAngle = BattingCalculator.AdjustBallAngle(Hit_HorizontalAngle + 0x800)

        iVar2 = BUNTING_POWER_ARRAY[self.inMemBatter["Batter_ContactType"]][1] - \
                BUNTING_POWER_ARRAY[self.inMemBatter["Batter_ContactType"]][0]
        self.Hit_HorizontalPower = (self.StaticRandomInt1 - (self.StaticRandomInt1 / iVar2) * iVar2) + \
                                   BUNTING_POWER_ARRAY[self.inMemBatter["Batter_ContactType"]][0]

        self.inMemBatter["AtBat_Mystery_CaptainStarSwing"] = 0
        return

    def calculateHorizontalAngle(self):
        input = self.inMemBatter["ControllerInput"]

        isCharge = 1 if self.inMemBatter["Batter_Contact_SlapChargeBuntStar"] != SLAP else 0
        self.inMemBatter["AtBat_InputDirection"] = PUSHPULL_NONE
        if (self.inMemBatter["AtBat_Mystery_BatDirection"] == 0):
            if (not input["Right"]):
                if (input["Left"]):
                    if (self.inMemBatter["AtBat_BatterHand"] == RIGHTY):
                        self.inMemBatter["AtBat_InputDirection"] = PUSHPULL_PULL

                    else:
                        self.inMemBatter["AtBat_InputDirection"] = PUSHPULL_PUSH

            elif (self.inMemBatter["AtBat_BatterHand"] == RIGHTY):
                self.inMemBatter["AtBat_InputDirection"] = PUSHPULL_PUSH

            else:
                self.inMemBatter["AtBat_InputDirection"] = PUSHPULL_PULL

        inputDirection = self.inMemBatter["AtBat_InputDirection"]
        frameOfContact = self.inMemBatter["Frame_SwingContact1"]
        iVar2 = BATTING_ANGLE_RANGES[inputDirection][isCharge][frameOfContact][0]
        iVar1 = BATTING_ANGLE_RANGES[inputDirection][isCharge][frameOfContact][1]

        self.Display_Output["Horizontal Range"] = [
            BATTING_ANGLE_RANGES[inputDirection][isCharge][frameOfContact][0] + 0x400,
            BATTING_ANGLE_RANGES[inputDirection][isCharge][frameOfContact][1] + 0x400
        ]

        iVar1 -= iVar2
        if (iVar1 < 0):
            iVar2 += self.StaticRandomInt1 - BattingCalculator.floor(self.StaticRandomInt1 / -iVar1) * -iVar1

        elif (0 < iVar1):
            iVar2 += self.StaticRandomInt1 - BattingCalculator.floor(self.StaticRandomInt1 / iVar1) * iVar1

        iVar2 += 0x400
        if (self.inMemBatter["AtBat_BatterHand"] != RIGHTY):
            if (iVar2 < 0x801):
                iVar2 = 0x800 - iVar2

            else:
                iVar2 = 0x1800 - iVar2

        self.Hit_HorizontalAngle = BattingCalculator.AdjustBallAngle(iVar2)

        if "override_horizontal_angle" in self.readValues:
            self.Hit_HorizontalAngle = self.readValues["override_horizontal_angle"]

    def calculateVerticalAngle(self):
        iVar5 = 0
        upDown = 0
        slapOrCharge = 0 if self.inMemBatter["Batter_Contact_SlapChargeBuntStar"] == 0 else 1
        pInput = self.inMemBatter["ControllerInput"]

        handledVerticalZones = False

        captainStarSwing = self.inMemBatter["AtBat_Mystery_CaptainStarSwing"]
        if (captainStarSwing == 0):
            if (self.inMemBatter["AtBat_MoonShot"] == False):
                noncaptainStarSwing = self.inMemBatter["nonCaptainStarSwingContact"]
                if (noncaptainStarSwing == 0):
                    if (self.inMemBatter["AtBat_Mystery_BatDirection"] == 0):
                        if (not pInput["Up"]):
                            if (pInput["Down"]):
                                # 2 == Down
                                upDown = 2

                        else:
                            # 1 == Up
                            upDown = 1

                    pabVar4 = BATTING_VERTICAL_ANGLE_WEIGHTS[self.inMemBatter["AtBat_HitTrajectoryLow"]][slapOrCharge][
                        self.inMemBatter["EasyBatting"]][self.inMemBatter["Batter_ContactType"]]
                    local_28 = pabVar4[0]
                    local_27 = pabVar4[1]
                    local_26 = pabVar4[2]
                    local_25 = pabVar4[3]
                    local_24 = pabVar4[4]

                    uVar4 = UINT_ARRAY_ARRAY_807B7134[self.inMemBatter["Batter_HitType"]][
                        3 - self.inMemBatter["EasyBatting"]]
                    uVar6 = UINT_ARRAY_ARRAY_807B7134[self.inMemBatter["Batter_HitType"]][4]
                    uVar5 = uVar4 & 0xf000000
                    if (uVar5 == 0):
                        uVar16 = uVar4 & 0xf
                        if (uVar16 != 0):
                            iVar5 = 2
                            if (uVar16 == 2):
                                if (upDown == 2):
                                    iVar5 = 0
                                    uVar6 = 2

                            elif ((uVar16 == 3) and (upDown == 1)):
                                iVar5 = 0
                                uVar6 = 2

                    else:
                        iVar5 = 1
                        if (uVar5 == 0x2000000):
                            if (upDown == 2):
                                iVar5 = 0
                                uVar6 = 2

                        elif ((uVar5 == 0x3000000) and (upDown == 1)):
                            iVar5 = 0
                            uVar6 = 2

                    if (uVar6 == 1):
                        DAT_80893800_VertAngle = 2

                    elif (uVar6 == 2):
                        DAT_80893800_VertAngle = 3

                    if (iVar5 == 0):
                        if ((uVar4 & 0x1e0) == 0):
                            local_28 = 0

                        if ((uVar4 & 0xf0) == 0):
                            local_27 = 0

                        if ((uVar4 & 0x78) == 0):
                            local_26 = 0

                        if ((uVar4 & 0x3c) == 0):
                            local_25 = 0

                        if ((uVar4 & 0x1e) == 0):
                            local_24 = 0

                        if (upDown == 2):
                            local_24 += local_28
                            local_28 = 0

                        elif (upDown == 1):
                            cVar2 = local_24 + local_28
                            local_24 = 0
                            local_28 = local_25 + cVar2
                            local_25 = 0

                    if (iVar5 == 0):
                        weightedRandomIndex = self.WeightedRandomIndex(
                            [local_28, local_27, local_26, local_25, local_24], 5)

                        if "override_vertical_range" in self.readValues:
                            weightedRandomIndex = self.readValues["override_vertical_range"]

                        # Regular star swings
                        lowerRange = \
                        SHORT_ARRAY_ARRAY_ARRAY_ARRAY_807B67CC[slapOrCharge][self.inMemBatter["Batter_ContactType"]][
                            weightedRandomIndex][0]
                        higherRange = \
                        SHORT_ARRAY_ARRAY_ARRAY_ARRAY_807B67CC[slapOrCharge][self.inMemBatter["Batter_ContactType"]][
                            weightedRandomIndex][1]

                        self.Display_Output["Vertical Details"] = {
                            "Zones": SHORT_ARRAY_ARRAY_ARRAY_ARRAY_807B67CC[slapOrCharge][
                                self.inMemBatter["Batter_ContactType"]],
                            "Weights": [local_28, local_27, local_26, local_25, local_24],
                            "Selected Zone": weightedRandomIndex
                        }

                        handledVerticalZones = True

                    else:
                        lowerRange = SHORT_ARRAY_ARRAY_807B6AF4[iVar5][0]
                        higherRange = SHORT_ARRAY_ARRAY_807B6AF4[iVar5][1]

                else:
                    # Non Captain Star Swings
                    lowerRange = NON_CAPTAIN_STAR_VERTICAL_ANGLES[
                        noncaptainStarSwing - 1][self.inMemBatter["Batter_ContactType"]][0]
                    higherRange = NON_CAPTAIN_STAR_VERTICAL_ANGLES[
                        noncaptainStarSwing - 1][self.inMemBatter["Batter_ContactType"]][1]

            else:
                # Moonshot, also uses Charge Angles
                lowerRange = SHORT_ARRAY_ARRAY_ARRAY_ARRAY_807B67CC[1][self.inMemBatter["Batter_ContactType"]][2][0]
                higherRange = SHORT_ARRAY_ARRAY_ARRAY_ARRAY_807B67CC[1][self.inMemBatter["Batter_ContactType"]][2][1]

        else:
            # Captain Star Swings
            lowerRange = CAPTAIN_STAR_VERTICAL_ANGLES[captainStarSwing - 1][self.inMemBatter["Batter_ContactType"]][0]
            higherRange = CAPTAIN_STAR_VERTICAL_ANGLES[captainStarSwing - 1][self.inMemBatter["Batter_ContactType"]][1]

        if (not handledVerticalZones):
            self.Display_Output["Vertical Details"] = {
                "Zones": [[lowerRange, higherRange]],
                "Weights": [100],
                "Selected Zone": 0
            }

        self.Display_Output["Vertical Details"]["Selected Range"] = [lowerRange, higherRange]

        sVar3 = lowerRange + (self.StaticRandomInt1 - BattingCalculator.floor(self.StaticRandomInt1 /
                                                                              (higherRange - lowerRange)) * (
                                          higherRange - lowerRange))

        self.Hit_VerticalAngle = sVar3

        if "override_vertical_angle" in self.readValues:
            self.Hit_VerticalAngle = self.readValues["override_vertical_angle"]

        if (self.Hit_VerticalAngle < 0x401):
            if (self.Hit_VerticalAngle < -0x400):
                self.Hit_VerticalAngle += 0x1000
                self.Hit_HorizontalAngle = BattingCalculator.AdjustBallAngle(self.Hit_HorizontalAngle + 0x800)

            elif (self.Hit_VerticalAngle < 0):
                self.Hit_VerticalAngle += 0x1000

        else:
            self.Hit_VerticalAngle = 0x800 - self.Hit_VerticalAngle
            self.Hit_HorizontalAngle = BattingCalculator.AdjustBallAngle(self.Hit_HorizontalAngle + 0x800)

    def calculateHitPower(self):
        uVar2 = 0
        niceSour = self.inMemBatter["Batter_ContactType"]
        charged = self.inMemBatter["BatterAtPlate_BatterCharge_Up"]

        # Regular contact array
        contactArray = BALL_HIT_ARRAY[self.inMemBatter["Batter_Contact_SlapChargeBuntStar"]][niceSour]

        if (self.inMemBatter["AtBat_Mystery_CaptainStarSwing"] == 0):
            if (self.inMemBatter["nonCaptainStarSwingContact"] != 0):
                charged = 0.0
                # NonCaptainStarSwing array
                contactArray = STAR_SWING_EXIT_VELOCITY_ARRAY[self.inMemBatter["nonCaptainStarSwingContact"] - 1][
                    niceSour]

        else:
            charged = 0.0
            # CaptainStarSwingArray
            contactArray = \
            CAPTAIN_STAR_SWING_EXIT_VELOCITY_ARRAY[self.inMemBatter["AtBat_Mystery_CaptainStarSwing"] - 1][niceSour]

        if (self.inMemBatter["AtBat_Mystery_DidPopFlyOrGrounderConnect"] != False):
            self.inMemBatter["BatterAtPlate_BatterCharge_Down"] = 1.0

        if (self.inMemBatter["AtBat_MoonShot"]):
            # Moonshot array
            contactArray = BALL_HIT_ARRAY[1][self.inMemBatter["Batter_ContactType"]]

        # Low value
        arrayV1 = contactArray[0]
        # High Value
        arrayV2 = contactArray[1]
        # 0x44 is a range 0-1 towards the better contact
        calcedDistance = self.inMemBatter["ContactQuality"] * (arrayV2 - arrayV1) + arrayV1
        # Non star swing
        if (self.inMemBatter["AtBat_Mystery_CaptainStarSwing"] == 0):
            if (charged <= 0.0):
                # If not charged, use slap hit power
                power = self.inMemBatter["Batter_SlapHitPower"]

            else:
                # use charge power
                power = (self.inMemBatter["BatterAtPlate_ChargePower"] - (
                            self.inMemBatter["BatterAtPlate_ChargePower"] - self.inMemBatter[
                        "Batter_SlapHitPower"]) * 0.5 * (1.0 - self.inMemBatter["BatterAtPlate_BatterCharge_Down"]))

        else:
            # if star swing, power is always 100
            power = 100.0

        if ((self.inMemBatter["AtBat_Mystery_CaptainStarSwing"] == 0) and (
                self.inMemBatter["nonCaptainStarSwingContact"] == 0)):
            perfectNiceSour = 2
            if ((self.inMemBatter["Batter_ContactType"] == LEFT_NICE) or (
                    self.inMemBatter["Batter_ContactType"] == RIGHT_NICE)):
                perfectNiceSour = 1

            elif (self.inMemBatter["Batter_ContactType"] == PERFECT):
                perfectNiceSour = 0

            dVar3 = BattingCalculator.LinearInterpolateToNewRange(self.inMemPitcher["calced_cursedBall"], 0.0, 100.0,
                                                                  CURSED_BALL_DEBUFF_ARRAY[perfectNiceSour][0],
                                                                  CURSED_BALL_DEBUFF_ARRAY[perfectNiceSour][1])
            power = (power * dVar3)

        if ((self.inMemBatter["RandomBattingFactors_ChemLinksOnBase"] != 0) and (0.0 < charged)):
            # If charging, add a multiplier for chem on base
            power = (
                    power * POWER_CHEM_LINK_MULTIPLIERS[self.inMemBatter["RandomBattingFactors_ChemLinksOnBase"]])

        if (-1 < self.inMemBatter["Batter_HitType"]):
            power = (
                            power * UINT_ARRAY_ARRAY_807B7134[self.inMemBatter["Batter_HitType"]][
                        1 - self.inMemBatter["EasyBatting"]]) / 100.0

        fVar1 = (calcedDistance * ((power / 100.0) * (1.0 - 0.8) + 0.8))

        self.AddedContactGravity = 0.00001 * contactArray[2]

        self.Display_Output["PowerDetails"] = {
            "CalculatedCharacterPower": power,
            "CalculatedContactPower": calcedDistance,
            "AddedGravity": contactArray[2],
        }

        if (self.inMemBatter["AtBat_Mystery_CaptainStarSwing"] == 0):
            ballAngle = self.Hit_HorizontalAngle
            if (ballAngle < 0x200):
                niceSour = 0

            elif (ballAngle < 0x601):
                niceSour = ballAngle - 0x200

            else:
                niceSour = 0x400

            if (self.inMemBatter["AtBat_BatterHand"] != RIGHTY):
                niceSour = 0x400 - niceSour

            if (niceSour < 0x100):
                iVar1 = 0

            elif (niceSour < 0x200):
                iVar1 = 1
                niceSour -= 0x100

            elif (niceSour < 0x300):
                iVar1 = 2
                niceSour -= 0x200

            else:
                iVar1 = 3
                niceSour -= 0x300

            fieldAreaBonus = BattingCalculator.LinearInterpolateToNewRange(
                (niceSour / 256), 0.0, 1.0,
                FIELD_TRAJECTORY_BONUSES[self.inMemBatter["BatterAtPlate_TrajectoryNearFar"]][iVar1],
                FIELD_TRAJECTORY_BONUSES[self.inMemBatter["BatterAtPlate_TrajectoryNearFar"]][iVar1 + 1])
            self.Display_Output["PowerDetails"]["FieldBonus"] = fieldAreaBonus
            fVar1 = (fVar1 * fieldAreaBonus)
        else:
            self.Display_Output["PowerDetails"]["FieldBonus"] = 0.0
        if (self.inMemBatter["AtBat_MoonShot"]):
            fVar1 = (fVar1 * MOONSHOT_MULTIPLIER)

        if "override_power" in self.readValues:
            fVar1 = self.readValues["override_power"]

        self.Hit_HorizontalPower = BattingCalculator.floor(fVar1)
        return

    def isEmptyOrSpaces(s: str):
        return True if len(s) == 0 else s.isspace()

    def parseValues(self):
        self.Display_Output = {}
        self.inMemBall = {}
        self.inMemPitcher = {}
        self.inMemPitcher["calced_cursedBall"] = STATS[self.readValues["pitcher_id"]]["Cursed Ball"]
        pitcherChargeVal = self.readValues["pitcherChargeVal"]
        if (pitcherChargeVal == 0):
            self.inMemPitcher["Pitcher_TypeOfPitch"] = PITCHCURVE
            self.inMemPitcher["ChargePitchType"] = PITCHCHARGETYPE_NONE

        elif (pitcherChargeVal == 1):
            self.inMemPitcher["Pitcher_TypeOfPitch"] = PITCHCHARGE
            self.inMemPitcher["ChargePitchType"] = PITCHCHARGETYPE_CHARGE

        elif (pitcherChargeVal == 2):
            self.inMemPitcher["Pitcher_TypeOfPitch"] = PITCHCHARGE
            self.inMemPitcher["ChargePitchType"] = PITCHCHARGETYPE_PERFECT

        elif (pitcherChargeVal == 3):
            self.inMemPitcher["Pitcher_TypeOfPitch"] = PITCHCHANGEUP
            self.inMemPitcher["ChargePitchType"] = PITCHCHARGETYPE_NONE

        self.StaticRandomInt1 = None
        self.StaticRandomInt2 = None
        self.USHORT_8089269c = None

        if (self.readValues["StaticRandomInt1"] != None):
            self.StaticRandomInt1 = self.readValues["StaticRandomInt1"]
        else:
            self.StaticRandomInt1 = BattingCalculator.floor(random() * 2 ** 15)

        if (self.readValues["StaticRandomInt2"] != None):
            self.StaticRandomInt2 = self.readValues["StaticRandomInt2"]
        else:
            self.StaticRandomInt2 = BattingCalculator.floor(random() * 2 ** 15)

        if (self.readValues["USHORT_8089269c"] != None):
            self.USHORT_8089269c = self.readValues["USHORT_8089269c"]
        else:
            self.USHORT_8089269c = BattingCalculator.floor(random() * 2 ** 15)

        self.inMemBatter = {}
        id = self.readValues["batter_id"]

        self.inMemBatter["Batter_CharID"] = id
        self.inMemBatter["IsCaptain"] = self.readValues["IsCaptain"]
        self.inMemBatter["Name"] = STATS[id]["Name"]
        self.inMemBatter["AtBat_Mystery_BatDirection"] = 0
        self.inMemBatter["AtBat_TrimmedBat"] = 0 if BATTER_HITBOXES[id]["TrimmedBat"] == 0.0 else 1

        self.inMemBatter["ballContact_X"] = self.readValues["ballContact_X"]
        self.inMemBatter["ballContact_Z"] = self.readValues["ballContact_Z"]
        self.inMemBatter["posX"] = self.readValues["posX"]

        self.inMemBatter["AtBat_BatterHand"] = self.readValues["AtBat_BatterHand"]

        self.inMemBatter["Batter_Contact_SlapChargeBuntStar"] = self.readValues["Batter_Contact_SlapChargeBuntStar"]
        self.inMemBatter["Batter_IsBunting"] = self.inMemBatter["Batter_Contact_SlapChargeBuntStar"] == BUNT

        self.inMemBatter["BatterAtPlate_BatterCharge_Up"] = self.readValues["chargeUp"]
        self.inMemBatter["BatterAtPlate_BatterCharge_Down"] = self.readValues["chargeDown"]
        self.inMemBatter["AtBat_IsFullyCharged"] = self.inMemBatter["BatterAtPlate_BatterCharge_Up"] == 1.0

        self.inMemBatter["Batter_SlapHitPower"] = STATS[id]["Slap Hit Power"]
        self.inMemBatter["BatterAtPlate_ChargePower"] = STATS[id]["Charge Hit Power"]

        self.inMemBatter["Batter_SlapContactSize"] = STATS[id]["Slap Contact Spot Size"]
        self.inMemBatter["Batter_ChargeContactSize"] = STATS[id]["Charge Contact Spot Size"]
        self.inMemBatter["Batter_Bunting"] = STATS[id]["Bunting"]

        self.inMemBatter["BatterAtPlate_TrajectoryNearFar"] = STATS[id]["Horizontal Hit Trajectory"]
        self.inMemBatter["AtBat_HitTrajectoryLow"] = STATS[id]["Vertical Hit Trajectory"]

        self.inMemBatter["RandomBattingFactors_ChemLinksOnBase"] = self.readValues[
            "RandomBattingFactors_ChemLinksOnBase"]
        self.inMemBatter["Frame_SwingContact1"] = self.readValues["frameOfContact"]

        self.inMemBatter["EasyBatting"] = self.readValues["EasyBatting"]
        self.inMemBatter["isStar"] = self.readValues["isStar"]

        self.inMemBatter["AtBat_MoonShot"] = False

        self.inMemBatter["ControllerInput"] = {
            "Up": self.readValues["Up"],
            "Down": self.readValues["Down"],
            "Left": self.readValues["Left"],
            "Right": self.readValues["Right"]
        }

        self.inMemBatter["AtBat_CaptainStarHitPitch"] = STATS[id]["Captain Star Hit/Pitch"]
        self.inMemBatter["AtBat_NonCaptainStarSwing"] = STATS[id]["Non Captain Star Swing"]

        self.inMemBatter["nonCaptainStarSwingContact"] = 0
        self.inMemBatter["nonCaptainStarSwingContact"] = 0
        self.inMemBatter["AtBat_Mystery_CaptainStarSwing"] = 0
        self.inMemBatter["AtBat_Mystery_DidPopFlyOrGrounderConnect"] = False

        self.inMemBatter["Stars"] = self.readValues["numStars"]

        if (self.readValues["is_starred"]):
            self.inMemBatter["Batter_SlapContactSize"] = min(self.inMemBatter["Batter_SlapContactSize"] + 50, 100)
            self.inMemBatter["Batter_ChargeContactSize"] = min(self.inMemBatter["Batter_ChargeContactSize"] + 50, 100)

            self.inMemBatter["Batter_SlapHitPower"] = min(self.inMemBatter["Batter_SlapHitPower"] + 50, 100)
            self.inMemBatter["BatterAtPlate_ChargePower"] = min(self.inMemBatter["BatterAtPlate_ChargePower"] + 50, 100)
            self.inMemBatter["Batter_Bunting"] = min(self.inMemBatter["Batter_Bunting"] + 50, 100)

            self.inMemPitcher["calced_cursedBall"] = min(self.inMemPitcher["calced_cursedBall"] + 50, 100)

    def hitBall(self):
        fVar1 = self.inMemBatter["ballContact_X"]

        if (BATTING_REACHES[self.inMemBatter["AtBat_TrimmedBat"]][0] <= fVar1 - self.inMemBatter["posX"]):
            if (fVar1 - self.inMemBatter["posX"] <= BATTING_REACHES[self.inMemBatter["AtBat_TrimmedBat"]][1]):
                self.inMemBatter["interstitialBallContact_X"] = fVar1
                return True

        return False

    def mssbConvertToRadians(param_1):
        if (param_1 < 0):
            param_1 += 0x1000

        if (0xfff < param_1):
            param_1 += -0x1000

        dVar1 = (math.pi * (param_1 << 1)) / 4096
        if (math.pi < dVar1):
            dVar1 = -(2 * math.pi - dVar1)

        return dVar1

    def convertPowerToVelocity(self):
        self.inMemBall["ballVelocity"] = {"X": 0, "Y": 0, "Z": 0}
        self.inMemBall["ballAcceleration"] = {"X": 0, "Y": 0, "Z": 0}

        half_power = self.Hit_HorizontalPower * 0.5

        horizontalAngle = BattingCalculator.mssbConvertToRadians(self.Hit_HorizontalAngle)
        verticalAngle = BattingCalculator.mssbConvertToRadians(self.Hit_VerticalAngle)

        s_verticalAngle = math.sin(verticalAngle)
        c_verticalAngle = math.cos(verticalAngle)

        half_power_x_cos_vert_angle = half_power * c_verticalAngle

        c_horizontalAngle = math.cos(horizontalAngle)
        s_horizontalAngle = math.sin(horizontalAngle)

        x_groundVelocity = c_horizontalAngle * half_power_x_cos_vert_angle
        z_groundVelocity = s_horizontalAngle * half_power_x_cos_vert_angle

        self.inMemBall["ballVelocity"]["X"] = x_groundVelocity / 100.0
        self.inMemBall["ballVelocity"]["Y"] = (half_power * s_verticalAngle) / 100.0
        self.inMemBall["ballVelocity"]["Z"] = z_groundVelocity / 100.0

        self.inMemBall["ballAcceleration"]["X"] = 0.0
        self.inMemBall["ballAcceleration"]["Y"] = self.AddedContactGravity
        self.inMemBall["ballAcceleration"]["Z"] = 0.0

        if ((self.inMemBatter["Batter_IsBunting"] == False) and (
                self.Hit_HorizontalAngle < 0x901 or 0xeff < self.Hit_HorizontalAngle)):
            # has Super Curve
            hasSuperCurve = 1 if self.inMemBatter["Batter_CharID"] in [
                0xe, 0x35, 0x25] else 0

            # non-captain star swing 3 has super curve
            if (self.inMemBatter["nonCaptainStarSwingContact"] == 3):
                hasSuperCurve = 1

            # if contact above 100, flip it
            contact = self.inMemBatter["CalculatedBallPos"]
            if (100.0 < self.inMemBatter["CalculatedBallPos"]):
                contact = 200.0 - self.inMemBatter["CalculatedBallPos"]

            vAngle = self.Hit_VerticalAngle
            fVar1 = (1.0 - (1.0 - contact * 0.01) *
                     FLOAT_ARRAY_ARRAY_807B72BC[hasSuperCurve][0])

            if ((0x180 < vAngle) and (vAngle < 0x401)):
                uVar3 = vAngle - 0x180
                contact = uVar3
                if (512.0 < uVar3):
                    contact = 512.0

                fVar1 = fVar1 * (1.0 - contact * 1.0 / 512.0)

            hAngle = self.Hit_HorizontalAngle

            if ((hAngle < 0xc01) and (0xff < hAngle)):
                if (0x700 < hAngle):
                    hAngle = 0x700

            else:
                hAngle = 0x100

            if (self.inMemBatter["AtBat_BatterHand"] != RIGHTY):
                hAngle = 0x800 - hAngle

            if (hAngle < 0x460):
                contact = (0x460 - hAngle) / 864.0

            else:
                contact = (0x460 - hAngle) / 672.0

            contact = (fVar1 * contact)
            if (0.0 <= contact):
                if (0.0 < contact):
                    z_groundVelocity = -c_horizontalAngle
                    x_groundVelocity = s_horizontalAngle

            else:
                contact = -contact
                z_groundVelocity = c_horizontalAngle
                x_groundVelocity = -s_horizontalAngle

            # finalize acceleration
            self.inMemBall["ballAcceleration"]["Z"] = (
                                                              z_groundVelocity * contact) * \
                                                      FLOAT_ARRAY_ARRAY_807B72BC[hasSuperCurve][2]
            self.inMemBall["ballAcceleration"]["X"] = (
                                                              x_groundVelocity * contact) * \
                                                      FLOAT_ARRAY_ARRAY_807B72BC[hasSuperCurve][1]

            # if z is backwards, flip it
            if (0.0 < self.inMemBall["ballAcceleration"]["Z"]):
                self.inMemBall["ballAcceleration"]["Z"] = -self.inMemBall["ballAcceleration"]["Z"]

            # if batting lefty, flip it
            if (self.inMemBatter["AtBat_BatterHand"] != RIGHTY):
                self.inMemBall["ballAcceleration"]["X"] = -self.inMemBall["ballAcceleration"]["X"]

        self.Display_Output["BallDetails"] = {
            "HorizontalAngle": self.Hit_HorizontalAngle,
            "VerticalAngle": self.Hit_VerticalAngle,
            "Power": self.Hit_HorizontalPower,

            "Velocity": self.inMemBall["ballVelocity"],
            "Acceleration": self.inMemBall["ballAcceleration"],
        }

    def calculateHitGround(self):
        p = {"X": self.inMemBatter["ballContact_X"],
             "Y": BATTER_HITBOXES[self.inMemBatter["Batter_CharID"]]["PitchingHeight"],
             "Z": self.inMemBatter["ballContact_Z"]}
        if self.inMemBatter["AtBat_BatterHand"] != RIGHTY:
            p["X"] = -p["X"]

        CalculatedPoints = []

        v = {k: v for k, v in self.inMemBall["ballVelocity"].items()}
        a = {k: v for k, v in self.inMemBall["ballAcceleration"].items()}

        airResistance = 0.996
        gravity = 0.00275

        while (p["Y"] > 0):
            CalculatedPoints.append({k: v for k, v in p.items()})

            p["X"] = p["X"] + v["X"]
            p["Y"] = p["Y"] + v["Y"]
            p["Z"] = p["Z"] + v["Z"]

            v["X"] = v["X"] * airResistance + a["X"]
            v["Y"] = (v["Y"] - gravity) * airResistance + a["Y"]
            v["Z"] = v["Z"] * airResistance + a["Z"]

        self.Display_Output["FlightDetails"] = {
            "Frames": len(CalculatedPoints),
            "HitGround": CalculatedPoints[-1],
            "Distance": math.sqrt(CalculatedPoints[-1]["X"] ** 2 + CalculatedPoints[-1]["Z"] ** 2),
            "Path": CalculatedPoints
        }
        # print(CalculatedPoints)

    def calculateValues(self):
        if (not self.hitBall()):
            self.Display_Output["err"] = "The ball would not hit the bat with these values"
            return

        starsForBatter = self.inMemBatter["Stars"]
        if (self.inMemBatter["isStar"]):
            if (self.inMemBatter["Batter_IsBunting"] == False):
                if (starsForBatter != 0):
                    if ((self.inMemBatter["AtBat_IsFullyCharged"] == False) or (starsForBatter < 5)):
                        if (self.inMemBatter["AtBat_CaptainStarHitPitch"] == 0):
                            if ((starsForBatter < 1) or (self.inMemBatter["AtBat_NonCaptainStarSwing"] == 0)):
                                self.inMemBatter["isStar"] = False

                            else:
                                self.inMemBatter["nonCaptainStarSwingContact"] = self.inMemBatter[
                                    "AtBat_NonCaptainStarSwing"]
                                if (self.inMemBatter["AtBat_NonCaptainStarSwing"] == 2):
                                    self.inMemBatter["Batter_Contact_SlapChargeBuntStar"] = CHARGE
                                    self.inMemBatter["AtBat_Mystery_DidPopFlyOrGrounderConnect"] = True
                                    self.inMemBatter["BatterAtPlate_BatterCharge_Up"] = 1.0

                                elif (self.inMemBatter["AtBat_NonCaptainStarSwing"] < 2):
                                    if (self.inMemBatter["AtBat_NonCaptainStarSwing"] != 0):
                                        self.inMemBatter["Batter_Contact_SlapChargeBuntStar"] = CHARGE
                                        self.inMemBatter["AtBat_Mystery_DidPopFlyOrGrounderConnect"] = True
                                        self.inMemBatter["BatterAtPlate_BatterCharge_Up"] = 1.0

                                elif (self.inMemBatter["AtBat_NonCaptainStarSwing"] < 4):
                                    self.inMemBatter["Batter_Contact_SlapChargeBuntStar"] = SLAP

                        elif (self.inMemBatter["IsCaptain"]):
                            if (starsForBatter < 1):
                                self.inMemBatter["isStar"] = False

                            else:
                                self.inMemBatter["Batter_Contact_SlapChargeBuntStar"] = STAR

                        elif (starsForBatter < 2):
                            self.inMemBatter["isStar"] = False

                        else:
                            self.inMemBatter["Batter_Contact_SlapChargeBuntStar"] = STAR

                    else:
                        self.inMemBatter["Batter_Contact_SlapChargeBuntStar"] = STAR
                        self.inMemBatter["AtBat_MoonShot"] = True

                    if ((self.inMemBatter["Batter_Contact_SlapChargeBuntStar"] == STAR) or (
                            self.inMemBatter["AtBat_Mystery_DidPopFlyOrGrounderConnect"] != False)):
                        self.inMemBatter["AtBat_Mystery7"] = 0
                        self.inMemBatter["AtBat_Mystery_CaptainStarSwing"] = self.inMemBatter[
                            "AtBat_CaptainStarHitPitch"]

            else:
                self.inMemBatter["Batter_Contact_SlapChargeBuntStar"] = BUNT
                self.inMemBatter["AtBat_MoonShot"] = False

        self.calculateContact()
        if (not self.inMemBatter["Batter_IsBunting"]):
            self.calculateHorizontalAngle()

            self.calculateVerticalAngle()

            self.calculateHitPower()
        else:
            self.calculateBuntAngle()

            self.calculateBuntingExtras()

        self.convertPowerToVelocity()

        self.calculateHitGround()

        self.Display_Output["err"] = None

        return self.Display_Output

    def valueToDegrees(v):
        return (v / 4096) * 360

    def degreesToRadians(d):
        return d * math.pi / 180


def hit_ball(**kwargs) -> dict:
    """ Returns power, trajectory, and other information about hitting a ball.

    batter_id: int, default 0, (short) 80890972
    is_batter_captain: bool, default False
    pitcher_id: int, default 0, (short) 80890ada

    easy_batting: bool, default false, (bool) 8089098a
    handedness: int, (0) Righty, (1) Lefty, default 0, (bool) 8089098a

    batter_x: float, default 0.0, (float) 8089095c
    ball_x: float, default 0.0, (float) 80890934
    ball_z: float, default 0.0, (float) 8089093c

    chem: int, default 0, (byte) 808909ba

    num_stars: int, default 4, (Used to calculate if moonshot)

    hit_type: int, (0) Slap, (1) Charge, default 0, (byte) 8089099b
    is_star_hit: bool, default false, (bool) 808909b1
    is_starred: bool, default false

    pitch_type: int, (0)Curve (1)Charge (2)PerfectCharge (3)ChangeUp, default 0, (byte) 80890b21 (byte) 80890b1f

    charge_up, float, default 0.0, (float) 80890968
    charge_down, float, default 0.0, (float) 8089096c

    frame: int, default 2, (short) 80890976

    stick_up: bool, default false
    stick_down: bool, default false
    stick_left: bool, default false
    stick_right: bool, default false

    rand_1: int, default 0, (uint) 80892684
    rand_2: int, default 0, (uint) 80892688
    rand_3: int, default 0, (ushort) 8089269C
    """

    kwargs.setdefault("batter_id", 0)
    kwargs.setdefault("is_batter_captain", False)
    kwargs.setdefault("pitcher_id", 0)

    kwargs.setdefault("easy_batting", False)
    kwargs.setdefault("handedness", 0)

    kwargs.setdefault("batter_x", 0.0)
    kwargs.setdefault("ball_x", 0.0)
    kwargs.setdefault("ball_z", 0.0)

    kwargs.setdefault("chem", 0)
    kwargs.setdefault("num_stars", 4)

    kwargs.setdefault("hit_type", 0)
    kwargs.setdefault("is_star_hit", False)
    kwargs.setdefault("is_starred", False)

    kwargs.setdefault("pitch_type", 0)

    kwargs.setdefault("charge_up", 0.0)
    kwargs.setdefault("charge_down", 0.0)

    kwargs.setdefault("frame", 0)

    kwargs.setdefault("stick_up", False)
    kwargs.setdefault("stick_down", False)
    kwargs.setdefault("stick_left", False)
    kwargs.setdefault("stick_right", False)

    kwargs.setdefault("rand_1", 0)
    kwargs.setdefault("rand_2", 0)
    kwargs.setdefault("rand_3", 0)

    newArgs = {
        "batter_id": kwargs["batter_id"],
        "IsCaptain": kwargs["is_batter_captain"],
        "pitcher_id": kwargs["pitcher_id"],

        "EasyBatting": kwargs["easy_batting"],
        "AtBat_BatterHand": kwargs["handedness"],

        "posX": kwargs["batter_x"],
        "ballContact_X": kwargs["ball_x"],
        "ballContact_Z": kwargs["ball_z"],

        "RandomBattingFactors_ChemLinksOnBase": kwargs["chem"],

        "Batter_Contact_SlapChargeBuntStar": kwargs["hit_type"],
        "isStar": kwargs["is_star_hit"],
        "is_starred": kwargs["is_starred"],

        "pitcherChargeVal": kwargs["pitch_type"],

        "chargeUp": kwargs["charge_up"],
        "chargeDown": kwargs["charge_down"],

        "frameOfContact": kwargs["frame"],

        "Up": kwargs["stick_up"],
        "Down": kwargs["stick_down"],
        "Left": kwargs["stick_left"],
        "Right": kwargs["stick_right"],

        "StaticRandomInt1": kwargs["rand_1"],
        "StaticRandomInt2": kwargs["rand_2"],
        "USHORT_8089269c": kwargs["rand_3"],

        "numStars": kwargs["num_stars"]
    }

    if "override_vertical_range" in kwargs:
        newArgs["override_vertical_range"] = kwargs["override_vertical_range"]

    if "override_vertical_angle" in kwargs:
        newArgs["override_vertical_angle"] = kwargs["override_vertical_angle"]

    if "override_horizontal_angle" in kwargs:
        newArgs["override_horizontal_angle"] = kwargs["override_horizontal_angle"]

    if "override_power" in kwargs:
        newArgs["override_power"] = kwargs["override_power"]

    c = BattingCalculator()

    c.readValues = newArgs
    c.parseValues()
    try:
        return c.calculateValues()
    except BaseException as e:
        return {"err": f"{e=}"}

# if __name__ == "__main__":
#     e = hit_ball(
#         batter_id = 2,
#         pitcher_id = 26,
#         easy_batting = False,
#         handedness = 0,
#         batter_x = 0.0,
#         ball_x = 0.2101,
#         ball_z = 0.0,
#         chem = 2,
#         hit_type = 0,
#         is_star_hit = False,
#         pitch_type = 3,
#         charge_up = 0.0,
#         charge_down = 0.0,
#         frame = 4,
#         rand_1 = 30677,
#         rand_2 = 2380,
#         rand_3 = 29261,
#         stick_down = True,
#         num_stars = 4,
#         is_starred = False,
#     )
#     print(json.dumps(e, sort_keys=True, indent=4))


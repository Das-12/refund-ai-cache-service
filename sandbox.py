import hashlib

text="""CHANGES
    ANY TIME
      CHARGE INR 2000 FOR REISSUE.
         NOTE -
          ABOVE CHARGES ARE EXCLUSIVE OF GST K3.
          APPLICABLE GST RATE TO BE COLLECTED AND SHOWN
          SEPARATELY UNDER TAX CODE K3.
          --------------------------------------------------
          A CHANGE IS A DATE/FLIGHT/ROUTING/BOOKING CODE
          MODIFICATION.
          --------------------------------------------
          CHARGE APPLIES PER TRANSACTION.
          A TRANSACTION MAY INCORPORATE ONE OR MORE
          RESERVATION CHANGE IN THE SAME TRANSACTION E.G.
          FLIGHT AND DATE CHANGE IN ONE DIRECTION OR BOTH.
          ---------------------------------------------
          CHARGE APPLIES TO ADULT AND CHILD.
          INFANT NOT OCCUPYING A SEAT IS EXEMPTED.
          --------------------------------------------------
          ANY DIFFERENCE IN FARE AND TAXES ALSO TO BE
          CHARGED IN ADDITION TO THE CHANGE PENALTY.
          --------------------------------------------------
          CHANGES FEE DOESNOT APPLY FOR UPGRADE TO A HIGHER
          CABIN CLASS ON THE SAME DAY FLIGHT.ONLY DIFFRENCE
          IN FARE AND TAXES TO BE COLLECTED.
          IF THE UPGRADE IS WITH A DATE /FLIGHT
          CHANGE THEN CHANGE FEE ALSO TO BE COLLECTED ALONG
          WITH DIFFRENCE IN FARE AND TAXES.
          --------------------------------------------------
          WHEN NOSHOW TICKET IS PRESENTED FOR
          REBOOKING/BOTH NOSHOW AND REBOOKING/REISSUE
          CHARGE APPLY.NO SHOW IS WHEN A PAX FAILS TO
          CHANGE BOOKING AT LEAST 4 HR BEFORE DEPARTURE OF
          THE FLIGHT CHANGED.
          ------------------------------------------------
          CANCELLING THE RESERVATION WITH NO ACTION ON THE
          TICKET WILL LEAD TO NO-SHOW PENALTY FEES.
          -------------------------------------------------
          TICKET HAS TO BE REISSUED FOR ANY CHANGE
          INCLUDING DATE/FLIGHT/ROUTING/BOOKING CHANGE.
          -----------------------------------------------
          REBOOKING/REISSUE/UPGRADING MUST BE MADE IN ONE
          TRANSACTION BEFORE DEPARTURE OF THE  FLIGHT BEING
          CHANGED.
          -------------------------------------------------
          REISSUE TO BE DONE BY THE ORIGINAL ISSUING
          AGENT OR UK OFFICE ONLY.
          --------------------------------------
          IF NO SEATS ARE AVAILABLE IN THE SAME RBD/FARE AS
          TICKETED PASSENGERS MAY BE BOOKED IN THE HIGHER
          RBD/FARE BY CHARGING DIFFERENCE OF FARE AND
          TAXES.DOWNSELLING TO A LOWER RBD/FARE IS NOT
          PERMITTED.
          --------------------------------------------------
          THE CHANGE/REISSUE CHARGE PLUS DIFFERENCE IN FARE
          AND TAXES WILL ALSO APPLY EVEN IF THERE IS A
          CHANGE OF DATE/FLIGHT/ROUTING/BOOKING ONLY ON THE
          INTERLINING SECTOR.
          ------------------------------------------------
          REPRICING SCENARIO
          1.BEFORE DEPARTURE/ FULLY UNUTILIZED TICKETS-
          BEFORE UTILIZATION OF THE FIRST COUPON OF THE
          TICKET WHEN VOLUNTARY CHANGE OCCURS IRRESPECTIVE
          OF OUTBOUND OR INBOUND FLIGHT OF THE JOURNEY THE
          FARE WILL BE RECALCULATED BY APPLYING NEW
          FARE/RULES ADHERING TO THE AP CONDITION IN EFFECT
          ON THE DATE OF REISSUE.
          2.AFTER DEPARTURE/ PARTIALLY UTILIZED TICKETS-
          AFTER UTILIZATION OF THE FIRST COUPON OF THE
          TICKET NEW FARE WILL BE RECALCULATED USING FARES
          AS PER ORIGINAL DATE OF ISSUE.
          --------------------------------------------------
          WHEN FARES ARE COMBINED THE MOST RESTRICTIVE
          CONDITIONS APPLY FOR THE ENTIRE JOURNEY.
          ------------------------------------------------
          THE CHANGE/REISSUE CHARGE IS NON - REFUNDABLE.
          -----------------------------------------------
          IN EVENT OF UPGRADE - THE ORIGINAL NON-REFUNDABLE
          AMOUNT WILL REMAIN NON-REFUNDABLE.
          ----------------------------------------------
          CHARGES ARE NON-COMMISISONABLE.  APPLICABLE GST
          WILL BE ADDITIONAL
          ------------------------------------------------
          THE RULES OF INTERNATIONAL
          THROUGH FARE WILLTAKE PRECEDENCE OVER DOMESTIC
          FARE RULES IN CASE OF COMBINATION OF FARES.
          -------------------------------------------------
          THE ABOVE CHARGE HAS TO BE CONVERTED INTO
          LOCAL CURRENCY AT THE BANKERS SELLING RATE.
          ---------------------------------------------
          INCASE OF INTERNATIONAL-DOMESTIC END ON END FARE
          COMBINATION
          PENALTIES WOULD APPLY PER FARE COMPONENT FOR
          CHANGES/REFUND AND CANCELLATIONS
  CANCELLATIONS
    ANY TIME
      CHARGE INR 3000 FOR REFUND.
         NOTE -
          ABOVE CHARGES ARE EXCLUSIVE OF GST K3.
          APPLICABLE GST RATE TO BE COLLECTED AND
          ADDED TO THE PENALTY AMOUNT.
          --------------------------------------------------
          CHARGE APPLIES TO ADULT AND CHILD.
          INFANT NOT OCCUPYING A SEAT IS EXEMPTED.
          ------------------------------------------------
          APPLICABLE PENALTIES TO BE RECOVERED FROM THE
          BASIC FARE AND FUEL CHARGE ONLY.
          ------------------------------------------
          IN CASES WHERE THE APPLICABLE PENALTIES ARE
          HIGHER THAN THE SUM OF THE BASIC FARE AND FUEL
          CHARGE/ ONLY THE BASIC FARE AND FUEL CHARGE WILL
          BE FORFEITED. ONLY STATUTORY TAXES AND OTHER
          CHARGES.LIKE AIRPORT DEPARTURE TAX ETC.TO BE
          REFUNDED IN FULL.
          -----------------------------------------------
          AGAINST NON - REFUNDABLE TICKETS ONLY THE BASIC
          FARE AND FUEL CHARGE TO BE FORFEITED. STATUTORY
          TAXES AND OTHER CHARGES ARE REFUNDABLE IN FULL.
          --------------------------------------------------
          IN CASE OF PARTIALLY UTILIZED TICKETS CHARGE ONE
          WAY FARE OR HALF ROUND TRIP FARE WHICHEVER IS
          HIGHER IN THE SAME RBD FOR THE SECTOR UTILISED
          PLUS APPLICABLE TAXES.
          IF NO ONE WAY FARE EXISTS FOR THE UTILISED SECTOR
          IN THE SAME RBD THE NEXT HIGHER RBD WILL APPLY IN
          ADDITION TO THE CANCELLATION CHARGE.
          ----------------------------------------------
          IN CASE OF CHANGE TO HIGHER RBD FOR TRAVEL ON THE
          SAME DAY/SAME FLIGHT/RE-ISSUANCE FEE WILL NOT BE
          APPLICABLE.ONLY DIFFERENCE IN TOTAL FARE IS TO BE
          COLLECTED.
          --------------------------------------------------
          OUT OF SEQUENCE TRAVEL NOT PERMITTED
          THERE WILL BE NO REFUND FOR OUT OF SEQUENCE COUPON
          EXCEPT THE STATUTARY TAXES.
          -------------------------------------------------
          THE CANCELLATION CHARGE WILL APPLY EVEN IF THERE
          IS CANCELLATION ONLY OF THE INTERLINING SECTOR.
          --------------------------------------------------
          WHEN FARES ARE COMBINED THE MOST RESTRICTIVE
          CONDITIONS APPLY FOR THE ENTIRE JOURNEY.
          -------------------------------------------------
          THE CHANGE/REISSUE CHARGE IS NON - REFUNDABLE.
          -----------------------------------------------
          CHARGES ARE NON-COMMISISONABLE.  APPLICABLE GST
          WILL BE ADDITIONAL.
          --------------------------------------------------
          IF A NON-REFUNDABLE TICKET IS RE-ISSUED TO A
          REFUNDABLE FARE THE ORIGINAL NON-REFUNDABLE
          AMOUNT WILL REMAIN NON-REFUNDABLE
          -----------------------------------------------
          THE ABOVE CHARGE HAS TO BE CONVERTED INTO
          LOCAL CURRENCY AT THE BANKERS SELLING RATE.
          --------------------------------------------
          INCASE OF INTERNATIONAL-DOMESTIC END ON END FARE
          COMBINATION
          PENALTIES WOULD APPLY PER FARE COMPONENT FOR
          CHANGES/REFUND AND CANCELLATIONS
      CHARGE INR 4000 FOR NO-SHOW.
         NOTE -
          ABOVE CHARGES ARE EXCLUSIVE OF GST K3.
          APPLICABLE GST RATE TO BE COLLECTED AND
          ADDED TO THE PENALTY AMOUNT.
          -------------------------------------------------
          NO SHOW IS WHEN A PAX FAILS TO CHANGE/CANCEL
          BOOKING AT LEAST 4 HR BEFORE DEPARTURE OF THE
          FLIGHT BEING CHANGED/CANCELLED.
          -----------------------------------------------
          CHARGE APPLIES TO ADULT AND CHILD.
          INFANT NOT OCCUPYING A SEAT IS EXEMPTED.
          ------------------------------------------------
          WHEN NOSHOW TICKET IS PRESENTED FOR REBOOKING/
          BOTH NOSHOW AND REBOOKING/REISSUE CHARGES APPLY.
          WHEN NOSHOW TICKET IS PRESENTED FOR CANCELLATION/
          BOTH NOSHOW AND CANCELLATION CHARGES APPLY.
          THE NO-SHOW CHARGE WILL APPLY EVEN IF THERE IS
          NO-SHOW ONLY ON THE INTERLINING SECTOR.
          --------------------------------------------------
          WHEN FARES ARE COMBINED THE MOST RESTRICTIVE
          CONDITIONS APPLY FOR THE ENTIRE JOURNEY.
          -----------------------------------------------
          CHARGES ARE NON-COMMISISONABLE.  APPLICABLE GST
          WILL BE ADDITIONAL.
          --------------------------------------------------
          THE RULES OF INTERNATIONAL
          THROUGH FARE WILLTAKE PRECEDENCE OVER DOMESTIC
          FARE RULES IN CASE OF COMBINATION OF FARES.
          -------------------------------------------------
          THE ABOVE CHARGE HAS TO BE CONVERTED INTO
          LOCAL CURRENCY AT THE BANKERS SELLING RATE.
          --------------------------------------------------
          VOID NOT PERMITTED."""

print(hashlib.sha256(text.encode('utf-8')).hexdigest())
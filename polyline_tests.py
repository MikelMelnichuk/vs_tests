import polyline


polyline_str = r"ezdvBcps}Lt@W@F@BVKl@UK]Wc@}@kAOKBEzA{BdA}Ab@s@LBf@RjARZBv@?rAAfBIX?f@FLBf@^b@hATbAF~@BvB?hALjBHpCLjAVdAd@dAxCbGlA~BbBvCpAbD`AnCVpB\\hBf@nB|@tAb@f@RVXLbDj@jCl@nAf@`DbBdC`B`@b@HNN`@lA~DnAvBvB`G\\fA^p@j@z@~E`FbBpBxDfFXh@|@pD`@bB^fANd@\\`Bl@rBb@fATj@v@bBjBwCd@w@NB^B\\@\\K\\Q|AWZGXOPIRBb@K\\Kl@_@VOZWVI^Eh@Ov@KxCJ\\@\\K^@RMh@QhAMXKXY`@Q^SLK`@]fBc@n@M\\OlB_@n@KNMRUZQZGh@Ht@Lx@F`@BTANDRNTPNDDHLXN`@LRTJx@?RBJFFLV\\Zs@TQ`@MVIhAYp@YPc@VgALk@Hk@d@eA\\cAHq@Eo@J}@@q@DItAgAv@i@|@e@v@k@bAaAdDuB|@c@?I?]?{@Ms@COFWJODYEcABOTU^e@H_@Km@Ci@BU?e@Ca@Ie@e@oBKk@Eu@M{@CoAC}@Km@Iy@IaA?{@Ci@Ms@UgA]y@Mm@GQICe@QKMGi@Gi@GSI[Ym@[{@@_AK]SMo@i@OCg@EOEMMYSi@IUO]Ko@KSIWUWMU_@I]Kw@WoACY@a@CWQWe@[QIOYMYW]SMQUQu@OWWSUWU[SsAEg@Ic@Mc@?a@Ai@Em@AUOa@M_@e@g@MSGYOY_@YIQSR[Pa@mBQaAI[@QDyACq@Iu@o@k@e@Y]IcAAmBC]Ee@IgAUWAw@Ae@GWSaAeAYk@Si@a@k@YAc@O{@]a@MnAqA~@mCVaAHk@YmCIQSQOS"


def decode_polyline(polyline_str):
    index, lat, lng = 0, 0, 0
    coordinates = []
    changes = {"latitude": 0, "longitude": 0}

    # Coordinates have variable length when encoded, so just keep
    # track of whether we've hit the end of the string. In each
    # while loop iteration, a single coordinate is decoded.
    while index < len(polyline_str):
        # Gather lat/lon changes, store them in a dictionary to apply them later
        for unit in ["latitude", "longitude"]:
            shift, result = 0, 0

            while True:
                byte = ord(polyline_str[index]) - 63
                index += 1
                result |= (byte & 0x1F) << shift
                shift += 5
                if not byte >= 0x20:
                    break

            if result & 1:
                changes[unit] = ~(result >> 1)
            else:
                changes[unit] = result >> 1

        lat += changes["latitude"]
        lng += changes["longitude"]

        coordinates.append((lat / 100000.0, lng / 100000.0))

    return coordinates


x = polyline.decode(polyline_str)
# x = decode_polyline(polyline_str)


print(x)
print(len(x))

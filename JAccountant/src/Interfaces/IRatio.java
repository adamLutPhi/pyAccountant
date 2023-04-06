package Interfaces;

public interface IRatio {

    Double cashRatio(Double cash, Double CurrentLiabilities);

    Double currentRatio(Double CurrentAssets, Double CurrentLiabilities);

    Double quickRatio(Double cashEquivalents, Double aReceivable, Double currentLiabilities);
}

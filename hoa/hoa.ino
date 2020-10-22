#include <Wire.h>

void setup() {
  analogReadResolution(14);
  Serial.begin(1000000);
}

void loop() {
  int val = 0;
  while(true) {
    // This does six reads and then outputs the sum because that cuts down on the time wasted sending data over the line,
    // and lets us gather more data points per second. It doesn't give us quite as fine-grained a resolution, but this gets us
    // twice the sampling rate of writing every value read (approximately 10k/s vs 5k/s).
    // As the purpose of this is to compare relative gunshot loudnesses, this should be an okay tradeoff.
    // Gunshot noise is incredibly short (in terms of how long the max magnitude lasts), so this decreases the chance that it'll be missed completely,
    // at the cost of flattening it a little bit. Next time I'm out at the range I'll test this and see which is better, but for now, I'm guessing it's this.
    // 6 was chosen because it guarantees that the value written out will be at most 5 characters (plus newline), because the range is 0-16383
    val = analogRead(A29);
    val += analogRead(A29);
    val += analogRead(A29);
    val += analogRead(A29);
    val += analogRead(A29);
    val += analogRead(A29);
    Serial.println(val);
  }
}

#define G 13 
#define S 12 
#define C 11
#define B 10
#define Q1 9
#define Q2 8
#define Q3 7     

String inByt;

void setup() {
  pinMode(G, OUTPUT);
  pinMode(S, OUTPUT);
  pinMode(C, OUTPUT);
  pinMode(B, OUTPUT);
  pinMode(Q1, OUTPUT);
  pinMode(Q2, OUTPUT);
  pinMode(Q3, OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  //

}

void serialEvent() {
    inByt = Serial.readStringUntil('\n');
   
    if (inByt == "Gon") {
        digitalWrite(G, HIGH);
    } else if (inByt == "Goff") {
        digitalWrite(G, LOW);
    } else if (inByt == "Son") {
        digitalWrite(S, HIGH);
    } else if (inByt == "Soff") {
        digitalWrite(S, LOW);
    } else if (inByt == "Con") {
        digitalWrite(C, HIGH);
    } else if (inByt == "Coff") {
        digitalWrite(C, LOW);
    } else if (inByt == "Bon") {
        digitalWrite(B, HIGH);
    } else if (inByt == "Boff") {
        digitalWrite(B, LOW);
    } else if (inByt == "Q1on") {
        digitalWrite(Q1, HIGH);
    } else if (inByt == "Q1off") {
        digitalWrite(Q1, LOW);
    } else if (inByt == "Q2on") {
        digitalWrite(Q2, HIGH);
    } else if (inByt == "Q2off") {
        digitalWrite(Q2, LOW);
    } else if (inByt == "Q3on") {
        digitalWrite(Q3, HIGH);
    } else if (inByt == "Q3off") {
        digitalWrite(Q3, LOW);
    } else {
       // continue;
    }
}

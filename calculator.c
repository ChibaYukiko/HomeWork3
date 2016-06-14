#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int index,index2;

struct tokens_t{
  string type; // NUMBER, PLUS, MINUS ,MULTI, DIVIS
  float number;
};

tokens_t* insert(int n, tokens_t *tokens, string str){

  tokens_t tokens2[256];
  int i = index2;
  for(i; i<n+1; i--){
    tokens2[i+1] = tokens[i];
  }
  
  tokens2[n].type = str;
  index2++;
  return tokens2;
}

tokens_t readNumber(char* line){
  float number = 0;
  tokens_t token;
  token.type = "NUMBER";
  
  while((index<strlen(line)) && (('0' <=line[index]) && (line[index] <= '9'))){
    number = number*10 + (int)(line[index]-'0');
    index++;
    if((index<strlen(line)) && (line[index] == '.')){
      index ++;
      float keta = 0.1;
      while((index<strlen(line)) && (('0' <=line[index]) && (line[index] <= '9'))){
	number = number + int(line[index]-'0')*keta;
	keta = keta*0.1;
	index++;
      }
    }
  }
  token.number = number;

  return token;
}
  
tokens_t* tokensize(char* line){
  tokens_t tokens[256];
  index = 0;
  index2 = 0;

  while(index < strlen(line)){
    if(('0' <=line[index]) && (line[index] <= '9')){
      tokens[index2] = readNumber(line);
      index2++;
    }else if(line[index] == '+'){
      tokens[index2].type = 'PLUS';
      index++;
      index2++;
    }else if(line[index] == '-'){
      tokens[index2].type = 'MINUS';
      index++;
      index2++;
    }else if(line[index] == '*'){
      tokens[index2].type = 'MULTI';
      index++;
      index2++;
    }else if(line[index] == '/'){
      tokens[index2].type = 'DIVIS';
      index++;
      index2++;
    }else{
      printf("Invalid character found: %c\n", line[index]);
      exit(1);
    }
  }

  return *tokens;

}


tokens_t* evaluteMultiAndDivide(tokens_t *tokens){

  tokens_t tokens2[256],tokens3[256];

  tokens2 = insert(0, tokens, "MULTI");

  int i, j;
  float number;
  i = 1;
  j = 0;
  number = 1.0;

  while( i < index2 ){
    if(tokens2[i].type == "NUMBER"){
      if(tokens2[i-1].type == "MULTI"){
	number = number * tokens2[i].number;
      }else if(tokens2[i-1].type == "DIVIS"){
	number = number / tokens2[i].number;
      }else{
	number = tokens2[i].number;
      }
    }else if((tokens2[i].type == "PLUS")||(tokens2[i].type == "MINUS")){
      tokens3[j].type = "NUMBER";
      tokens3[j].number = number;

      j++;

      tokens3[j].type = tokens2[j].type;
      j++;
    }
    i++;
  }

  tokens3[j].type = "NUMBER";
  tokens3[j].number = number;

  index2 = j;
  
  return tokens3;
  
}


float  evalutePlusAndMinus(tokens_t *tokens){
  float answer = 0;
  tokens_t tokens2[256];

  tokens2 = insert(0, tokens, "PLUS");
  int i = 1;

  while( i <= index2 ){
    if(tokens2[i].type == "NUMBER"){
      if(tokens2[i-1].type == "PLUS"){
	answer = answer + tokens2[i].number;
      }else if(tokens2[i-1].type == "MINUS"){
	answer = answer - tokens2[i].number;
      }else{
	printf("Invalid Syntax\n");
      }
    }
    i++;
  }

  return answer; 
  
}

float evalute(tokens_t *tokens){

  tokens_t tokens2[256];
  float answer;

  tokens2 = evaluteMultiAndDivide(tokens);
  answer = evalutePlusAndMinus(tokens2);

}

int main(){
  char line[256];
  tokens_t tokens[256];
  float answer;
  
  while (true){
    printf("\n> ");
    scanf("%s",line);
    tokens = tokenize(line);
    answer = evalute(tokens):
    printf("\nanswer = %f\n",answer);
    }
  
}

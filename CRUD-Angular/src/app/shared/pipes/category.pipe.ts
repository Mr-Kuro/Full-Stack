import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'category'
})
export class CategoryPipe implements PipeTransform {

  transform(value: string): string[] {
    switch(value){
      case 'FrontEnd': return ['web'];
      case 'BackEnd': return ['computer']; 
      case 'Fullstack': return ['developer_board']; 
    }
    return ['code'];
  }

}

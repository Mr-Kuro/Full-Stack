import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'id'
})
export class IdPipe implements PipeTransform {

  transform(value: String): String {
    
    if (Number(value)) return 'dns';
    
    return '';
  }

}

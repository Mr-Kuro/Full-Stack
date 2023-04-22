import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'duration'
})
export class DurationPipe implements PipeTransform {

  transform(value: string): string {
    
    if (Number(value)) return 'av_timer'
    
    return '';
  }

}

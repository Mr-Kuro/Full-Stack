import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, tap } from 'rxjs';

import { Course } from '../models/course';


@Injectable({
  providedIn: 'root'
})
export class CoursesService {

  private readonly API = 'api/courses';

  constructor(
    private httpClient: HttpClient
  ) { }

  list(): Observable<Course[]> {
    /*let list = [
        { "_id":"1", "name":"Angular + spring-boot", "category": "fullstack", "duracao": "46516" },
        { "_id":"2", "name":"Angular", "category": "front end", "duracao": "46516" },
        { "_id":"2", "name":"Spring-boot", "category": "back end", "duracao": "46516" }
      ]*/

    // return of (list);
    return this.httpClient.get<Course[]>(this.API).pipe(
      // delay(1000),
      tap(list => console.log(list))
    )
  }

  save(record: Course) {
    let resultado;
    this.httpClient.post<Course>(this.API, record).subscribe(
      result => resultado = result,
      error =>  {resultado = error; console.log(error)}
      )

      // console.log(resultado)
      return resultado

    // console.log(record)
  }



}

import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CourseFormComponent } from './containers/course-form/course-form.component';

import { CoursesComponent } from './containers/courses/courses.component';
import { CourseResolver } from './guards/course.resolver';
import { Course } from './interfaces/course';

//olhar o ngRoutingModules
const routes: Routes = [
  { path:'', component: CoursesComponent },
  { path:'new', component: CourseFormComponent, resolve: { course: CourseResolver } },
  { path:'edit/:_id', component: CourseFormComponent, resolve: { course: CourseResolver } },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CoursesRoutingModule { }

package com.chendless.repositories;

import com.chendless.domain.DataModel;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface DataRepository extends CrudRepository<DataModel, String> {
}
